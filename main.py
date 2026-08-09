def simulate_bitcoin_halving_cycle():
    """
    Simulates Bitcoin's halving cycle and its simplified impact on supply and price.
    """
    START_YEAR = 2009
    END_YEAR = 2040
    INITIAL_BLOCK_REWARD = 50.0  # BTC per block
    HALVING_INTERVAL_YEARS = 4
    # Approximating blocks per year for simplicity (10 minutes/block * 6 blocks/hour * 24 hours * 365 days)
    BLOCKS_PER_YEAR = 52560  

    current_block_reward = INITIAL_BLOCK_REWARD
    total_circulating_supply = 0.0
    # A simplified price index to demonstrate the article's concept of price increases
    # after halvings (bull market periods). This is an illustrative model, not a prediction.
    price_index = 1.0

    print("--- Bitcoin Halving Cycle Simulation ---")
    print(f"{'Year':<5} | {'Block Reward (BTC)':<18} | {'New Supply (BTC/yr)':<19} | {'Total Supply (BTC)':<19} | {'Price Index (Illustrative)':<28}")
    print("-" * 110)

    # The first halving occurred in late 2012. Subsequent halvings are every 4 years.
    next_halving_year = 2012 

    for year in range(START_YEAR, END_YEAR + 1):
        # Apply general annual growth to the price index (reflecting demand/adoption)
        # This growth is applied every year after the start, before checking for halving.
        if year > START_YEAR:
            price_index *= 1.05 # Small annual growth (5%)

        # Check for halving event
        if year == next_halving_year:
            # Bitcoin halving event: Block reward is cut in half.
            current_block_reward /= 2
            # According to the article, halvings trigger significant price increases.
            # This is a simplified model to reflect that "bull market" effect, boosting
            # the price index on top of any annual growth for that year.
            price_index *= 2.5 # Illustrative boost to price index
            print(f"--- HALVING EVENT IN {year}! Block reward halved to {current_block_reward:.2f} BTC. Price index boosted. ---")
            next_halving_year += HALVING_INTERVAL_YEARS
            
        # Calculate new supply for the year
        new_supply_this_year = current_block_reward * BLOCKS_PER_YEAR
        total_circulating_supply += new_supply_this_year

        print(f"{year:<5} | {current_block_reward:<18.2f} | {new_supply_this_year:<19.2f} | {total_circulating_supply:<19.2f} | {price_index:<28.2f}")

    print("-" * 110)
    print("\nNote: The 'Price Index' is a highly simplified, illustrative model")
    print("      to demonstrate the concept of price reactions to halving events,")
    print("      as described in the article, and does not represent actual market predictions.")

if __name__ == "__main__":
    simulate_bitcoin_halving_cycle()
