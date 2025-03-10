# Brown Forecasting Club Website

## Build Commands
```bash
# Install dependencies
pdm install

# Build the static site (generates HTML in docs/ directory)
python ssg.py
```

## Project Structure
- `assets/`: Static assets (images)
- `docs/`: Output directory (used for GitHub Pages)
- `templates/`: Jinja2 HTML templates
- `ssg.py`: Static site generator script

## Code Style Guidelines
- **Python**: 
  - 4-space indentation
  - Snake case for variables/functions
  - Imports: standard library first, then third-party
  - Simple error handling with basic checks before operations

- **HTML/CSS**:
  - Semantic HTML with Jinja2 templating
  - Inline CSS in base.html
  - Utility classes for common styling patterns
  - Brown University branding colors (#C00404 red, #4E3629 brown)

## Development Workflow
1. Edit templates in `templates/`
2. Update assets in `assets/`
3. Run `python ssg.py`
4. Commit changes to deploy via GitHub Pages