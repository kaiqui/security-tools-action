# Security Pipeline GitHub Action

This `security-pipeline` action is a composite action that runs a suite of security analysis tools suitable for different application contexts: web, infrastructure as code (IaC), and mobile. Depending on the context, it utilizes a combination of well-known security tools like OWASP Dependency-Check, TruffleHog, Semgrep, MobSF, and Checkov.

## Usage

You can incorporate this action into your GitHub Actions workflow to perform security scans across your application's codebase. It will automatically save the generated reports to a `reports` directory, which you can then upload as artifacts or use in subsequent steps.

### Inputs

- `context`: The context of the application you want to run the security tools against (`web`, `iac`, or `mobile`).
- `g_token`: Your GitHub Personal Access Token (PAT), used for authentication with various tools and GitHub itself.
- `g_username`: Your GitHub Username, used in conjunction with your PAT for authentication purposes.

### Outputs

- Security reports are saved in a `reports` folder at the root of the repository.

### Example Workflow

Here's how you can use this action in your `.github/workflows/security.yml` file:

```yaml
name: Security Pipeline

on: [push]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        
      - name: Run Security Pipeline
        uses: your-username/security-pipeline@v1
        with:
          context: 'web' # or 'iac' or 'mobile'
          g_token: ${{ secrets.GITHUB_TOKEN }}
          g_username: 'your-github-username'
        
      - name: Upload Security Reports to Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: security-reports
          path: reports/
```

### Tools Description

- `OWASP Dependency-Check`: Identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities.
- `TruffleHog`: Searches through git repositories for secrets, digging deep into commit history and branches.
- `Semgrep`: Static code analysis tool for finding bugs and enforcing code standards.
- `MobSF`: Automated security testing for Android, iOS, and Windows applications.
- `Checkov`: Static code analysis tool for infrastructure as code (IaC).

### Contributing

This action is open source and contributions are welcome. You can customize and extend it to fit your own security analysis needs.

### License

This project is distributed under the MIT License, allowing everyone to use, modify, and distribute it as they see fit.

### Acknowledgments

Thanks to all the contributors of the tools used in this action for providing the community with such valuable resources.