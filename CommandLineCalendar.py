import argparse  # Importing the argparse module for parsing command-line arguments
import calendar  # Importing the calendar module for calendar-related functions

def view_calendar(year, month):
    """Display the calendar for a specified year and month."""
    cal = calendar.month(year, month)  # Generate the calendar for the specified year and month
    print(cal)  # Print the generated calendar

def main():
    # Create an ArgumentParser object with a description of the program
    parser = argparse.ArgumentParser(description='Command-Line Calendar')

    # Define the '--view' option that expects two integer values: year and month
    parser.add_argument('--view', metavar=('YEAR', 'MONTH'), nargs=2, type=int,
                        help='View calendar for specified year and month')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the '--view' option was provided and contains two values
    if args.view is not None and len(args.view) == 2:
        year, month = args.view  # Extract the year and month values
        view_calendar(year, month)  # Call the view_calendar function to display the calendar
    else:
        parser.print_help()  # Print the help message if the '--view' option is missing or incomplete

if __name__ == '__main__':
    main()  # Execute the main function if the script is executed directly

# In Command you need to write: python [Name of File].py --view #### ## [YEAR] [Month]