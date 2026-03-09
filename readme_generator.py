import os
from datetime import datetime


def get_user_input():
    """Collect project details from user."""
    print("\n" + "=" * 50)
    print("   README.md Generator")
    print("=" * 50 + "\n")

    details = {}

    details['project_name'] = input("Project Name: ").strip()
    details['description'] = input("Project Description: ").strip()
    details['author'] = input("Author Name: ").strip()
    details['github_username'] = input("GitHub Username: ").strip()
    details['python_version'] = input("Python Version (e.g. 3.9): ").strip() or "3.9"
    details['license'] = input("License (e.g. MIT): ").strip() or "MIT"

    print("\nInstallation Steps (press Enter twice when done):")
    install_steps = []
    while True:
        step = input(f"  Step {len(install_steps) + 1}: ").strip()
        if not step:
            break
        install_steps.append(step)
    details['install_steps'] = install_steps

    print("\nUsage Examples (press Enter twice when done):")
    usage_examples = []
    while True:
        example = input(f"  Example {len(usage_examples) + 1}: ").strip()
        if not example:
            break
        usage_examples.append(example)
    details['usage_examples'] = usage_examples

    print("\nFeatures (press Enter twice when done):")
    features = []
    while True:
        feature = input(f"  Feature {len(features) + 1}: ").strip()
        if not feature:
            break
        features.append(feature)
    details['features'] = features

    return details


def generate_badges(details):
    """Generate shields.io badges."""
    username = details['github_username']
    repo = details['project_name'].lower().replace(' ', '-')
    python_version = details['python_version']
    license_type = details['license']

    badges = f"""![Python](https://img.shields.io/badge/python-{python_version}-blue.svg)
![License](https://img.shields.io/badge/license-{license_type}-green.svg)
![GitHub stars](https://img.shields.io/github/stars/{username}/{repo}?style=social)
![GitHub forks](https://img.shields.io/github/forks/{username}/{repo}?style=social)"""

    return badges


def generate_readme(details):
    """Generate README.md content."""

    install_content = ""
    if details['install_steps']:
        for i, step in enumerate(details['install_steps'], 1):
            install_content += f"{i}. {step}\n"
    else:
        install_content = "1. Clone the repository\n2. Install dependencies\n3. Run the project\n"

    usage_content = ""
    if details['usage_examples']:
        for example in details['usage_examples']:
            usage_content += f"```bash\n{example}\n```\n\n"
    else:
        usage_content = "```bash\npython main.py\n```\n"

    features_content = ""
    if details['features']:
        for feature in details['features']:
            features_content += f"- {feature}\n"
    else:
        features_content = "- Feature 1\n- Feature 2\n"

    badges = generate_badges(details)

    readme = f"""# {details['project_name']}

{badges}

## Description

{details['description']}

## Features

{features_content}
## Installation

{install_content}
## Usage

{usage_content}
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the {details['license']} License - see the [LICENSE](LICENSE) file for details.

## Author

**{details['author']}**
- GitHub: [@{details['github_username']}](https://github.com/{details['github_username']})

---
*Generated with README Generator on {datetime.now().strftime('%Y-%m-%d')}*
"""
    return readme


def save_readme(content, filename="README.md"):
    """Save README to file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nREADME.md generated successfully -> {os.path.abspath(filename)}")


def main():
    details = get_user_input()
    readme_content = generate_readme(details)
    print("\n" + "=" * 50)
    print("PREVIEW:")
    print("=" * 50)
    print(readme_content[:500] + "...")
    save_readme(readme_content)


if __name__ == "__main__":
    main()
