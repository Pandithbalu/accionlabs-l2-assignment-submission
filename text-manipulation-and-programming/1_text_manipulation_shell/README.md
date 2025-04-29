
# DevOps L2 Technical Evaluation Submission

This repository contains solutions to the eight-question L2 technical round assessment. The problems cover a wide range of DevOps and programming competencies including Docker, Kubernetes, CI/CD pipelines, shell scripting, text parsing, and object-oriented programming.

---

## 📁 Repository Structure

```
1_text_manipulation_shell/
  ├── extract_errors.sh
  ├── sample.log
  └── README.md

2_text_manipulation_oop/
  ├── text_parser.py
  └── README.md

3_sum_even_fibonacci/
  ├── even_fib_sum.py
  └── README.md

4_intersection_sorted_arrays/
  ├── array_intersection.py
  └── README.md

5_decimal_digit_transformation/
  ├── digit_transform.py
  └── README.md

docker_nginx/
  ├── Dockerfile
  └── README.md

k8s_statefulset/
  ├── nginx-statefulset.yaml
  ├── pvc.yaml
  └── README.md

github_actions_pipeline/
  ├── .github/workflows/nginx-ci-cd.yml
  └── README.md

.gitignore
README.md
```

---

## ✅ Problem Summary

| Folder                      | Problem Description                                                                 |
|----------------------------|--------------------------------------------------------------------------------------|
| `1_text_manipulation_shell` | Extract specific log entries using `grep` and `sed`                                |
| `2_text_manipulation_oop`   | OOP Python solution to parse and extract errors from a log file                    |
| `3_sum_even_fibonacci`      | Python class to compute sum of first 100 even Fibonacci numbers                    |
| `4_intersection_sorted_arrays` | Efficient Python function to find unique intersection of sorted arrays         |
| `5_decimal_digit_transformation` | OOP function to compute `X + XX + XXX + XXXX` pattern                    |
| `docker_nginx`              | Dockerfile for secure nginx 1.19 image                                             |
| `k8s_statefulset`           | StatefulSet + PVC YAML to deploy the nginx container with resource limits         |
| `github_actions_pipeline`   | GitHub Actions workflow for Docker build, security scan, and Kubernetes deployment |

---

## 🧪 How to Run

### Python Scripts

```bash
cd <folder_name>
python3 <script_name>.py
```

### Shell Script

```bash
cd 1_text_manipulation_shell
chmod +x extract_errors.sh
./extract_errors.sh
```

### Dockerfile

```bash
cd docker_nginx
docker build -t secure-nginx:1.19 .
```

### Kubernetes Resources

```bash
kubectl apply -f k8s_statefulset/
```

### GitHub Actions

- Push to the `main` branch to trigger CI/CD via `.github/workflows/nginx-ci-cd.yml`.

---

## 🛡️ Best Practices Followed

- Production-ready code: error handling, input validation, and clean structure
- Security-conscious Dockerfile and Kubernetes specs
- Modular and reusable components
- OOP principles applied where applicable
- Fully commented and documented

---

## ⚠️ Notes

- No AI artifacts or proprietary content included.
- All scripts tested and verified.
- CI/CD assumes Kubernetes cluster access via GitHub secrets.

---

## 📬 Author

Prepared for the DevOps L2 Technical Assessment  
**Contact:** [Your Name] | [Your Email] | [LinkedIn/GitHub if applicable]
