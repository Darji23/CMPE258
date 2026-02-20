# 🧠 MNIST Neural Network Classifier with Keras

A beginner-friendly neural network built with Keras to classify handwritten digits from the MNIST dataset — complete with training, evaluation, and rich visualizations.

---

## 🚀 Getting Started

Open the notebook directly in Google Colab:

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click **File → Upload Notebook**
3. Upload `mnist_classifier.ipynb`
4. Click **Runtime → Run All**

No additional setup or installs required.

---

## 📁 File

| File | Description |
|------|-------------|
| `mnist_classifier.ipynb` | Main Colab notebook with model, training, and evaluation |

---

## 🏗️ Model Architecture

| Layer | Units | Activation |
|-------|-------|------------|
| Input | 784 (flattened 28×28) | — |
| Dense + BatchNorm + Dropout | 512 | ReLU |
| Dense + BatchNorm + Dropout | 256 | ReLU |
| Dense + BatchNorm + Dropout | 128 | ReLU |
| Output | 10 | Softmax |

- **Optimizer:** Adam (lr=0.001)  
- **Loss:** Sparse Categorical Crossentropy  
- **Callbacks:** EarlyStopping, ReduceLROnPlateau

---

## 📊 Metrics & Visualizations Included

- Training/validation accuracy, loss, and top-3 accuracy curves
- Confusion matrix (raw counts + normalized)
- Per-class accuracy bar chart
- Full classification report (precision, recall, F1)
- ROC curves with AUC for all 10 digit classes
- Confidence distribution (correct vs. incorrect predictions)
- Calibration plot
- Misclassified sample viewer
- Final summary dashboard (Accuracy, F1, MCC, Mean AUC, Error Rate)

---

## 🛠️ Requirements

| Library | Version |
|---------|---------|
| TensorFlow / Keras | ≥ 2.x |
| NumPy | ≥ 1.21 |
| Matplotlib | ≥ 3.4 |
| Seaborn | ≥ 0.11 |
| Scikit-learn | ≥ 0.24 |

All libraries come pre-installed in Google Colab.

---

## 📈 Expected Results

| Metric | Value |
|--------|-------|
| Test Accuracy | ~98.5% |
| Macro F1 Score | ~0.985 |
| Mean ROC-AUC | ~0.9997 |

---

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
