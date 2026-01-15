import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def read_csv(p: Path) -> pd.DataFrame:
    if not p.exists():
        raise FileNotFoundError(str(p))
    return pd.read_csv(p)


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def save_plot(fig, out_path: Path):
    ensure_dir(out_path.parent)
    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    if not out_path.exists():
        raise RuntimeError(f"Plot was not saved: {out_path}")


def choose_xcol(df: pd.DataFrame):
    for c in ["iter", "k", "step", "i", "t", "index"]:
        if c in df.columns:
            return c
    return None


def choose_status_col(df: pd.DataFrame):
    for c in ["status", "SSE_status", "decision", "outcome"]:
        if c in df.columns:
            return c
    return None


def is_single_or_terminal(df: pd.DataFrame):
    if len(df) <= 1:
        return True
    sc = choose_status_col(df)
    if sc is None:
        return False
    s = df[sc].astype(str).str.upper()
    if s.isin(["ABSTAIN", "DENY", "ABSTAIN_SINGULAR", "ABSTAIN_UNDEFINED"]).any():
        # if a run contains terminal states, still ok to plot, but summary is also useful
        return False
    return False


def plot_series(df: pd.DataFrame, xcol: str, ycol: str, title: str, out_png: Path, ylog: bool = False, hline=None, hline_label=None):
    if xcol not in df.columns or ycol not in df.columns:
        return False

    # Only numeric y
    y = pd.to_numeric(df[ycol], errors="coerce")
    x = pd.to_numeric(df[xcol], errors="coerce")

    mask = x.notna() & y.notna()
    if mask.sum() == 0:
        return False

    x = x[mask].to_numpy()
    y = y[mask].to_numpy()

    fig = plt.figure()
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel(xcol)
    plt.ylabel(ycol)

    if ylog:
        y_pos = y[y > 0]
        if len(y_pos) == 0:
            plt.close(fig)
            return False
        plt.yscale("log")

    if hline is not None:
        plt.axhline(hline)
        if hline_label and len(x) > 0:
            plt.text(x[0], hline, hline_label)

    save_plot(fig, out_png)
    return True


def plot_text_summary(df: pd.DataFrame, out_png: Path, title: str):
    ensure_dir(out_png.parent)

    cols = list(df.columns)
    head = df.head(8)

    lines = []
    lines.append("COLUMNS:")
    lines.append(", ".join(cols) if cols else "(none)")
    lines.append("")
    lines.append("FIRST ROWS:")
    if len(head) == 0:
        lines.append("(empty CSV)")
    else:
        # compact table-like text
        lines.append(head.to_string(index=False))

    fig = plt.figure(figsize=(10, 6))
    plt.axis("off")
    plt.title(title)
    plt.text(0.01, 0.98, "\n".join(lines), va="top", family="monospace")
    save_plot(fig, out_png)


def plot_case2_folder(folder: Path, a_min=None, s_max=None, r_safe=None):
    trace = folder / "trace_sse.csv"
    df = read_csv(trace)

    plots_dir = folder / "plots"
    ensure_dir(plots_dir)

    xcol = choose_xcol(df)
    if xcol is None:
        # no x-axis; always summary
        plot_text_summary(df, plots_dir / "summary.png", f"{folder.name} (no x-axis column found)")
        return

    made_any = False

    # Prefer canonical columns if present, but don’t require them
    preferred = [
        ("a", False, a_min, "a_min"),
        ("s", False, s_max, "s_max"),
        ("err", True, None, None),
        ("r", False, r_safe, "r_safe"),
        ("risk", False, r_safe, "r_safe"),
    ]

    for ycol, ylog, hline, hlabel in preferred:
        if ycol in df.columns:
            title = f"{ycol} vs {xcol}"
            out = plots_dir / f"{ycol}_vs_{xcol}.png"
            made_any |= plot_series(df, xcol, ycol, title, out, ylog=ylog, hline=hline, hline_label=hlabel)

    # If none of the preferred plots were possible, fall back to summary
    if not made_any:
        plot_text_summary(df, plots_dir / "summary.png", f"{folder.name} (no preferred numeric columns plottable)")
        return

    # Always also produce a small summary (helps debug quickly)
    plot_text_summary(df, plots_dir / "summary.png", f"{folder.name} summary")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case2_root", required=True)
    ap.add_argument("--a_min", type=float, default=None)
    ap.add_argument("--s_max", type=float, default=None)
    ap.add_argument("--r_safe", type=float, default=None)
    args = ap.parse_args()

    root = Path(args.case2_root).resolve()
    if not root.exists():
        raise FileNotFoundError(str(root))

    csvs = list(root.rglob("trace_sse.csv"))
    if not csvs:
        raise RuntimeError(f"No trace_sse.csv found under: {root}")

    print(f"ROOT: {root}")
    print(f"Found {len(csvs)} trace_sse.csv files. Generating plots...")

    ok = 0
    for csv_path in csvs:
        folder = csv_path.parent
        plot_case2_folder(folder, a_min=args.a_min, s_max=args.s_max, r_safe=args.r_safe)
        plots_dir = folder / "plots"
        if not plots_dir.exists():
            raise RuntimeError(f"Expected plots folder missing: {plots_dir}")
        ok += 1
        print(f"OK (plots): {folder.name}")

    print(f"Done. Generated outputs for {ok} scenario folder(s).")


if __name__ == "__main__":
    main()
