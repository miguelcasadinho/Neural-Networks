import matplotlib
matplotlib.use('Agg')  # Use Agg backend for headless environments

import matplotlib.pyplot as plt

# Plotting the actual and predicted stock prices
plt.plot([1, 2, 3, 4, 5], color='red', label='Real Google Stock Price')
plt.plot([1.1, 1.9, 2.9, 4.1, 4.9], color='blue', label='Predicted Google Stock Price')

# Adding title and labels
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')

# Adding a legend
plt.legend()

# Save the plot to a file instead of displaying it
plt.savefig('stock_price_prediction.png')  # This will create a PNG file in your current directory