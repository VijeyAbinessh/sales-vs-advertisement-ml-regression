# sales-vs-advertisement-ml-regression

# 📊 Sales vs. Advertisement - Linear Regression Model

This project demonstrates a simple linear regression model to analyze and visualize the relationship between **sales** and **advertising expenditure** using Python and popular data science libraries.

## 📁 Project Structure

- **sales.txt**: Tab-separated dataset containing sales and advertisement values.
- **main.py**: Main Python script containing the data processing, model training, and visualization logic.

## 🧰 Libraries Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## 📈 Workflow

1. **Data Loading**  
   The dataset is loaded from a local `.txt` file with no headers and two columns: sales and advertisement.

2. **Preprocessing**  
   Data is reshaped and split into training and test sets using `train_test_split`.

3. **Modeling**  
   A linear regression model is trained using `LinearRegression` from `sklearn`.

4. **Evaluation**  
   - Model slope and intercept are printed.
   - Performance metrics like **Root Mean Squared Error (RMSE)** and **R² Score** are calculated.

5. **Visualization**  
   A scatter plot with the regression line is displayed to visualize the correlation.

## 🧪 Example Output

- **Estimated Model Slope (a)**: _printed to console_  
- **Estimated Model Intercept (b)**: _printed to console_  
- **RMSE**: _printed to console_  
- **R² Score**: _printed to console_

## 📌 How to Run

1. Clone the repository or download the `.py` file.
2. Ensure `sales.txt` is placed in the path specified.
3. Run the script:
   ```bash
   python main.py
   ```

## 📊 Sample Graph

The output includes a plot showing the regression line superimposed on the data points.

## ✍️ Author

Vijey Abinessh
