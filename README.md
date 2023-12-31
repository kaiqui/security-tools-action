# Security Tool Action

Esta ação do GitHub permite que você execute várias ferramentas de segurança no seu código.

## Ferramentas Disponíveis

- OWASP Dependency-Check
- Bandit
- Trufflehog

## Como Usar

Para usar uma das ferramentas de segurança em seu projeto, adicione o seguinte workflow ao seu repositório:

```yaml
name: Security Scan

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Run Security Tool
        uses: kaiqui/security-tool-action@main
        with:
          tool: web
          github_token: ${{ secrets.GITHUB_TOKEN }}
          github_username: ${{ secrets.GITHUB_USERNAME }}

