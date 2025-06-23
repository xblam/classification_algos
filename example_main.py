def main():
    # Load or create data
    X, y = load_data()

    # Define model type and complexity range
    model_type = 'decision_tree'
    complexity_range = range(1, 11)  # max_depth from 1 to 10

    # Estimate ideal complexity
    best_complexity, scores = find_optimal_complexity(
        X, y,
        model_type=model_type,
        complexity_range=complexity_range,
        scoring='accuracy',
        cv=5
    )

    print(f"Best complexity level: {best_complexity}")
    print(f"Scores across range: {scores}")