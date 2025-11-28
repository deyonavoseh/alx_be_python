class BankAccount:
    """A simple bank account class with deposit, withdraw, and balance display."""
    
    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional starting balance.
        
        Args:
            initial_balance (float): Starting balance, defaults to 0
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add funds to the account.
        
        Args:
            amount (float): Amount to deposit
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw funds from the account if sufficient balance exists.
        
        Args:
            amount (float): Amount to withdraw
        
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")