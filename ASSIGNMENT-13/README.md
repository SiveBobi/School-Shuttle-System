---

## 🚀 CI/CD Pipeline

This repo uses **GitHub Actions** for automated testing and artifact generation.

### ✅ CI (Test Pipeline)

- Runs `unittest` on every push and pull request.
- Ensures only working code reaches `main`.

### ✅ CD (Build Artifact)

- When code is merged into `main`:
  - Builds a Python package (`dist/*.whl`)
  - Uploads it as a release artifact

### ✅ Branch Protection Rules

- ❌ No direct push to `main`
- ✅ All PRs require at least 1 review
- ✅ All tests must pass before merging

📷 Screenshots:
- ![CI Success](docs/ci-success.png)
- ![Artifact Upload](docs/artifact-upload.png)
- ![PR Protection](docs/pr-protection.png)
- ![Branch Protection](docs/branch-protection.png)
