import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split


# ============================================================
# 1. LOAD DATASET
# ============================================================

DATA_PATH = r"Synergy_TP\task_13\data\train.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)
print(df.head())


# ============================================================
# 2. SEPARATE FEATURES AND LABEL
# ============================================================

# Target
y = df["label"].values

# Input pixels
X = df.drop("label", axis=1).values


# ============================================================
# 3. NORMALIZE PIXEL VALUES
# ============================================================

# Pixel values are normally 0-255
X = X / 255.0


# ============================================================
# 4. TRAIN-VALIDATION SPLIT
# ============================================================

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ============================================================
# 5. CONVERT TO PYTORCH TENSORS
# ============================================================

X_train = torch.tensor(X_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32)

y_train = torch.tensor(y_train, dtype=torch.long)
y_val = torch.tensor(y_val, dtype=torch.long)


# ============================================================
# 6. CREATE DATASETS
# ============================================================

train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)


# ============================================================
# 7. CREATE DATALOADERS
# ============================================================

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=64,
    shuffle=False
)


# ============================================================
# 8. DEFINE NEURAL NETWORK
# ============================================================

class NeuralNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(

            # 784 input pixels
            nn.Linear(784, 128),
            nn.ReLU(),

            nn.Linear(128, 64),
            nn.ReLU(),

            # 10 classes: digits 0-9
            nn.Linear(64, 10)
        )

    def forward(self, x):
        return self.network(x)


model = NeuralNetwork()

print("\nModel:")
print(model)


# ============================================================
# 9. LOSS FUNCTION
# ============================================================

criterion = nn.CrossEntropyLoss()


# ============================================================
# 10. OPTIMIZER
# ============================================================

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# ============================================================
# 11. TRAINING
# ============================================================

EPOCHS = 10

for epoch in range(EPOCHS):

    model.train()

    total_loss = 0

    for images, labels in train_loader:

        # Forward pass
        outputs = model(images)

        # Calculate loss
        loss = criterion(outputs, labels)

        # Clear gradients
        optimizer.zero_grad()

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)

    print(
        f"Epoch [{epoch + 1}/{EPOCHS}] "
        f"Loss: {average_loss:.4f}"
    )


# ============================================================
# 12. VALIDATION
# ============================================================

model.eval()

correct = 0
total = 0

with torch.no_grad():

    for images, labels in val_loader:

        outputs = model(images)

        # Get predicted class
        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()


accuracy = 100 * correct / total

print(f"\nValidation Accuracy: {accuracy:.2f}%")


# ============================================================
# 13. SAVE MODEL
# ============================================================

torch.save(
    model.state_dict(),
    "mnist_model.pth"
)

print("Model saved as mnist_model.pth")