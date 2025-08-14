# Cutting Stock API Requirements

## Functional Requirements

### Endpoints

- **/linear (POST)**: Solves 1D cutting problems (e.g., rods, pipes).
  - **Inputs** (JSON):
    - `stock_lengths`: List of stock lengths (e.g., [100, 120]).
    - `cut_lengths`: List of cut lengths (e.g., [30, 40]).
    - `quantities`: List of quantities (e.g., [3, 2]).
    - `kerf` (optional, default 0): Cut width.
    - `trims` (optional, default 0): Edge margins.
    - `costs` (optional, default None): Cost per stock.
    - `generate_svg` (optional, default False): Request SVG layout.
  - **Outputs** (JSON):
    - `stocks_used`: Number of stocks used.
    - `patterns`: List of cutting patterns.
    - `total_waste`: Total unused length.
    - `svg` (optional): Base64-encoded SVG.
- **/panel (POST)**: Solves 2D cutting problems (e.g., sheets).
  - **Inputs** (JSON):
    - `stock_widths`: List of stock widths (e.g., [100, 120]).
    - `stock_heights`: List of stock heights (e.g., [100, 100]).
    - `piece_widths`: List of piece widths (e.g., [30, 40]).
    - `piece_heights`: List of piece heights (e.g., [20, 30]).
    - `quantities`: List of quantities (e.g., [2, 2]).
    - `kerf` (optional, default 0): Cut width.
    - `trims` (optional, default 0): Edge margins.
    - `rotations_allowed` (optional, default False): Allow piece rotation.
    - `costs` (optional, default None): Cost per sheet.
    - `generate_svg` (optional, default False): Request SVG layout.
  - **Outputs** (JSON):
    - `panels_used`: Number of sheets used.
    - `layouts`: List of piece placements.
    - `total_waste`: Total unused area.
    - `svg` (optional): Base64-encoded SVG.

### Features

- Minimize waste or cost.
- Handle kerf and trims.
- Support rotations for 2D cutting.
- Generate SVG layouts.
- Validate inputs and handle errors.

## Non-Functional Requirements

- **Performance**: Solve typical inputs (100 cuts/pieces) in 2–5 seconds.
- **Scalability**: Handle large instances (500+ cuts/pieces).
- **Security**: API token authentication.
- **Usability**: JSON input/output, clear documentation.
- **Reliability**: Handle edge cases without crashing.
- **Extensibility**: Support future enhancements (e.g., irregular shapes).

## Algorithm Selection

- **1D Cutting**: Column Generation with ILP (OR-Tools).
- **2D Cutting**: Heuristics (e.g., Bottom-Left, Evolutionary) (OR-Tools).

## Tools and Libraries

- **Optimization**: OR-Tools (free, supports column generation).
- **API Framework**: Flask (lightweight, RESTful).
- **Visualization**: svgwrite (SVG generation).
- **Supporting**: NumPy (arrays), pytest (testing).
- **Optional**: opcut (specialized), deap (metaheuristics), Shapely (irregular shapes).

## Success Criteria

- Accurate cutting plans, verified against optima or optiCutter.
- Fast response (2–5 seconds for typical inputs).
- Robust error handling.
- Matches or exceeds optiCutter’s features.