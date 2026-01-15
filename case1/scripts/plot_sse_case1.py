import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _read_csv_if_exists(p: Path):
    if p.exists():
        return pd.read_csv(p)
    return None


def _save(fig, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)


def _plot_series(df, xcol, ycol, title, out_png, ylog=False, hline=None, hline_label=None):
    if xcol not in df.columns or ycol not in df.columns:
        return

    x = df[xcol].to_numpy()
    y = df[ycol].to_numpy()

    fig = plt.figure()
    plt.plot(x, y, marker="o", label=None if len(x) > 1 else "single-iteration trace")
    plt.title(title)
    plt.xlabel(xcol)
    plt.ylabel(ycol)

    if ylog:
        y_pos = y[y > 0]
        if len(y_pos) == 0:
            plt.close(fig)
            return
        plt.yscale("log")

    if hline is not None:
        plt.axhline(hline)
        if hline_label and len(x) > 0:
            plt.text(x[0], hline, hline_label)

    if len(x) <= 1:
        plt.legend(loc="best")

    _save(fig, out_png)


def _plot_status_summary_single(df_sse: pd.DataFrame, out_png: Path, a_min=None, s_max=None):
    row = df_sse.iloc[0].to_dict()

    keys_order = [
        "iter", "status", "SSE", "SSE_next", "improve_ratio", "a", "s", "step_norm", "cond",
        "b1", "b2", "b3", "b4", "b5"
    ]

    lines = []
    for k in keys_order:
        if k in row:
            v = row[k]
            if isinstance(v, float):
                lines.append(f"{k}: {v:.6g}")
            else:
                lines.append(f"{k}: {v}")

    if a_min is not None:
        lines.append(f"a_min: {a_min}")
    if s_max is not None:
        lines.append(f"s_max: {s_max}")

    fig = plt.figure(figsize=(8, 5))
    plt.axis("off")
    plt.title("SSE trace summary (single-iteration)")
    plt.text(0.02, 0.95, "\n".join(lines), va="top", family="monospace")
    _save(fig, out_png)


def plot_case1_folder(folder: Path, a_min=None, s_max=None):
    trace_sse_path = folder / "trace_sse.csv"
    df_sse = _read_csv_if_exists(trace_sse_path)
    if df_sse is None:
        raise FileNotFoundError(f"Missing {trace_sse_path}")

    plots_dir = folder / "plots"

    if "iter" in df_sse.columns and len(df_sse) <= 1:
        _plot_status_summary_single(
            df_sse,
            plots_dir / "summary_single_iteration.png",
            a_min=a_min,
            s_max=s_max,
        )
        return

    _plot_series(
        df_sse, "iter", "SSE",
        "SSE vs iter",
        plots_dir / "sse_vs_iter.png",
        ylog=False
    )

    _plot_series(
        df_sse, "iter", "a",
        "permission a vs iter",
        plots_dir / "a_vs_iter.png",
        ylog=False,
        hline=a_min,
        hline_label="a_min" if a_min is not None else None
    )

    _plot_series(
        df_sse, "iter", "s",
        "resistance s vs iter",
        plots_dir / "s_vs_iter.png",
        ylog=False,
        hline=s_max,
        hline_label="s_max" if s_max is not None else None
    )

    _plot_series(
        df_sse, "iter", "cond",
        "cond vs iter (log scale)",
        plots_dir / "cond_vs_iter.png",
        ylog=True
    )

    if "step_norm" in df_sse.columns:
        _plot_series(
            df_sse, "iter", "step_norm",
            "step_norm vs iter (log scale)",
            plots_dir / "step_norm_vs_iter.png",
            ylog=True
        )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case1_root", required=True, help="Path to 'Case 1' folder")
    ap.add_argument("--a_min", type=float, default=None)
    ap.add_argument("--s_max", type=float, default=None)
    ap.add_argument(
        "--folders",
        default="case1_abstain_singular,case1_deny_numeric,case1_allow_converged"
    )
    args = ap.parse_args()

    root = Path(args.case1_root)
    names = [x.strip() for x in args.folders.split(",") if x.strip()]

    for name in names:
        folder = root / name
        if folder.exists():
            plot_case1_folder(folder, a_min=args.a_min, s_max=args.s_max)

    print("Done. Plots saved under each scenario's 'plots' folder.")


if __name__ == "__main__":
    main()
