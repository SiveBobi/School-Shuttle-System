# 🔒 Branch Protection Rules – Explanation

To maintain code quality, integrity, and collaboration, we applied the following branch protection rules on the `main` branch:

---

## ✅ Applied Rules on `main`

1. **Require Pull Request Reviews:**
   - At least 1 reviewer must approve changes before merging.
   - Ensures peer review and reduces bugs.

2. **Require Status Checks to Pass:**
   - CI pipeline must succeed (tests must pass).
   - Prevents broken code from entering the production branch.

3. **Disallow Direct Pushes:**
   - Only pull requests can update `main`.
   - Prevents accidental commits or forced updates.

---

## 📌 Why It Matters

- 🛡️ Protects critical branches from accidental changes
- ✅ Enforces automated testing and code review culture
- 👥 Promotes collaborative development and CI/CD practices
- 🚫 Stops broken builds from being merged

---

These rules align with industry DevOps best practices and ensure that the project remains production-ready at all times.
