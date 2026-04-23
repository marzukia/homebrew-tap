# Changelog

All notable changes to Charted will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-23

### Added
- Zero-dependency SVG chart generation (bar, column, line, pie, scatter)
- Embedded font definitions for portable rendering
- CLI interface with batch processing
- Python API with theme support (10 built-in themes)
- Markdown integration (data URLs, inline SVG)
- HTML element generation
- Data transformation utilities
- Color palette utilities
- Visual regression testing
- Comprehensive documentation
- Portable zip bundle distribution

### Changed
- None

### Deprecated
- None

### Removed
- None

### Fixed
- None

### Security
- None

## [1.0.2] - 2026-04-23

### Fixed
- Homebrew formula installation fixes (brew tap marzukia/tap/charted)

### Changed
- None

### Deprecated
- None

### Removed
- None

### Added
- None

### Security
- None

## [1.0.1] - 2026-04-23

### Added
- Package manager install scripts (homebrew, apt, dnf, universal)
- Fallback to pipx/pip when system packages unavailable

### Fixed
- CLI usage examples in install readme
- Theme examples across chart documentation (pie.rst, scatter.rst)
- Theme count documentation (3 presets: dark, light, high-contrast)
- Theme dict structure documentation
- Duplicate sections and fake TOML/Theme constants in docs
- Sphinx documentation structure and API reference

### Changed
- Comprehensive documentation overhaul

### Deprecated
- None

### Removed
- Fake CLI section, fake theme sections, fake Theme constants

### Security
- None

## [0.1.0] - 2026-04-22

### Added
- Initial release
- All chart types and core functionality
