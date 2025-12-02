"""Main interactive application for the DATA3350 local project.
analyzer = Analyzer()
visualizer = Visualizer()


# Hold references to loaded DataFrames
datasets = {}


while True:
print_menu()
choice = input("Choose an option (1-6): ").strip()


if choice == "1":
print("Loading datasets...")
datasets['geo_map'] = loader.load_csv('geoMap.csv')
datasets['toy_raw'] = loader.load_json('toy-products-on-amazon-metadata.json')
datasets['amazon_raw'] = loader.load_csv('amazon_co-ecommerce_sample[1].csv')
print("Loaded keys:")
pprint.pprint(list(datasets.keys()))


elif choice == "2":
if 'amazon_raw' not in datasets:
print("Please load datasets first (option 1).")
continue
print("Cleaning amazon dataset...")
datasets['amazon_clean'] = cleaner.clean_amazon_df(datasets['amazon_raw'])
print("Cleaning toy JSON into DataFrame...")
datasets['toy_clean'] = cleaner.normalize_toy_json(datasets['toy_raw'])
print("Cleaning complete. Use option 3 to analyze or 4 to visualize.")


elif choice == "3":
if 'amazon_clean' not in datasets:
print("Please run cleaning first (option 2).")
continue
print("Running analysis...")
top_df = analyzer.top_rated_products(datasets['amazon_clean'], top_n=10)
avg_price = analyzer.avg_price_by_category(datasets['amazon_clean'])
print("Top rated products:\n")
print(top_df[['product_name','rating','price']])
print("\nAverage price by main category:\n")
print(avg_price)


elif choice == "4":
if 'amazon_clean' not in datasets:
print("Please run cleaning first (option 2).")
continue
print("Generating plots...")
visualizer.plot_price_distribution(datasets['amazon_clean'])
visualizer.plot_avg_price_by_category(datasets['amazon_clean'])


elif choice == "5":
out_dir = Path.cwd() / 'exported'
out_dir.mkdir(exist_ok=True)
if 'amazon_clean' in datasets:
save_dataframe_csv(datasets['amazon_clean'], out_dir / 'amazon_cleaned.csv')
print(f"Saved amazon_cleaned.csv to {out_dir}")
if 'toy_clean' in datasets:
save_dataframe_csv(datasets['toy_clean'], out_dir / 'toy_products.csv')
print(f"Saved toy_products.csv to {out_dir}")


elif choice == "6":
print("Goodbye!")
sys.exit(0)


else:
print("Invalid choice, please enter 1-6.")


if __name__ == '__main__':
main()
