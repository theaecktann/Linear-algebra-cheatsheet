import sys
from linalg import vector_basics, matrix_operations, eigen_decomposition
from visualizer import plot_vectors, plot_matrix_heatmap

def show_menu():
    print("\n" + "="*40)
    print("MatrixOps CheatSheet - Menu")
    print("="*40)
    print("1. Vectors and dot product")
    print("2. Matrix operations")
    print("3. Eigenvalues and eigenvectors")
    print("4. Generate all plots in ./assets/")
    print("0. Exit")
    print("="*40)

def main():
    print("Welcome to the interactive linear algebra cheat sheet!")
    while True:
        show_menu()
        choice = input("Select an option (0-4): ").strip()

        if choice == "1":
            v1, v2 = vector_basics()
            plot_vectors(v1, v2)
        elif choice == "2":
            A, B = matrix_operations()
            plot_matrix_heatmap(A)
        elif choice == "3":
            eigen_decomposition()
        elif choice == "4":
            print("\nGenerating all plots...")
            v1, v2 = vector_basics()
            plot_vectors(v1, v2)
            A, _ = matrix_operations()
            plot_matrix_heatmap(A)
            print("Done! Check the ./assets/ directory.")
        elif choice == "0":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()