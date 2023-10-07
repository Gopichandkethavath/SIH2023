import matplotlib.pyplot as plt
# from .compare import get_product_data


def plot_price_comparison(data):
    # Extract Flipkart and Amazon prices from the dataset
    flipkart_prices = [float(item["Price_x"][1:].replace(",", "")) for item in data]
    amazon_prices = [float(item["Price_y"].replace(",", "")) for item in data]

    # Create a list of product names (you can customize this based on your dataset)
    product_names = [item["Flipkart_Title"] for item in data]

    # Create a list of numbers representing the products (0, 1, 2, ...)
    product_numbers = list(range(len(data)))

    # Create the line graph
    plt.figure(figsize=(12, 6))
    plt.plot(
        product_numbers,
        flipkart_prices,
        marker="o",
        label="Flipkart Price",
        linestyle="-",
        color="b",
    )
    plt.plot(
        product_numbers,
        amazon_prices,
        marker="o",
        label="Amazon Price",
        linestyle="-",
        color="g",
    )

    # Customize the labels and title
    plt.xlabel("Product Number")
    plt.ylabel("Price (in INR)")
    plt.title("Flipkart vs. Amazon Price Comparison")

    # Customize the x-axis ticks and labels
    plt.xticks(product_numbers, product_names, rotation=90)

    # Show legend
    plt.legend()

    # Show the plot
    plt.tight_layout()
    save_path = r"D:\djangoproj\SIH2023\products_graph.png"
    plt.savefig(save_path)
    plt.show()


def count_favorable_products(data):
    favorable_to_flipkart = 0
    favorable_to_amazon = 0

    for item in data:
        flipkart_price = float(item["Price_x"][1:].replace(",", ""))
        amazon_price = float(item["Price_y"].replace(",", ""))

        # Compare prices to determine which platform is favorable
        if flipkart_price < amazon_price:
            favorable_to_flipkart += 1
        elif amazon_price < flipkart_price:
            favorable_to_amazon += 1

    return favorable_to_flipkart, favorable_to_amazon


def plot_favorable_products_pie(favorable_counts):
    labels = ["Favorable to Flipkart", "Favorable to Amazon"]
    sizes = [favorable_counts[0], favorable_counts[1]]
    colors = ["#ff9999", "#66b3ff"]
    explode = (0.1, 0)  # explode the 1st slice (Favorable to Flipkart)

    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        startangle=140,
    )
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Favorable Products Comparison")
    save_path = r"D:\djangoproj\SIH2023\products_piechart.png"
    plt.savefig(save_path)
    plt.show()


def save_graph(data) :
    # dataSet = get_product_data(search_query)
    print('called graph save')
    plot_price_comparison(data)
    favorable_counts = count_favorable_products(data)
    plot_favorable_products_pie(favorable_counts)