from concurrent.futures import ThreadPoolExecutor

import whois


def check_domain_availability(domain_name):
    """
    Check if a domain name is available.
    Args:
        domain_name (str): The domain name to check.
    Returns:
        tuple: A tuple containing the domain name and its availability status.
    """

    try:
        w = whois.whois(domain_name)
        if w.domain_name is None:
            return domain_name, "AVAILABLE"
        return domain_name, "NOT AVAILABLE"
    except Exception as e:
        print(f"Error checking domain {domain_name}: {e}")
        return domain_name, "NOT AVAILABLE"


def main(domain_list=None, tlds=None):
    """
    Main function to check domain availability.
    :param domain_list: List of domain names to check.
    :param tlds: List of top-level domains (TLDs) to check against.
    :return: 0 if successful, 1 if an error occurred.
    """
    if domain_list is None:
        domain_list = ["Mobix", "Zypix", "Qwelo", "Jynex", "Xymob", "Krylo",
                       "Veltu", "Syfon", "Nexmo", "Ryvex", "Zetix",
                       "Cymob", "Lymex", "Novlo", "Xyfon", "Fyber",
                       "Qwevo", "Jytel", "Vynix", "Zevlo", "Kryfi",
                       "Syvex", "Rivox", "Xybit", "Dynex", "Myqix", "Nexvu",
                       "Ryvix", "Zytel", "Cyvox", "Lymob", "Novex",
                       "Xylo", "Fytix", "Qwexo", "Jyvox", "Vynlo", "Zevix",
                       "Kryvo", "Sybit", "Rivlo", "Xytel", "Dynix",
                       "Myfon",
                       "Nexlo", "Ryvox", "Zytix", "Cyfon", "Lytel", "Novix"]

    if tlds is None:
        tlds = [".com"]

    # Prepare a list of full domain names
    full_domains = [f"{domain.lower()}{tld}" for domain in domain_list for tld in tlds]

    # Use ThreadPoolExecutor to check domains concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_domain_availability, full_domains)

    # Print results
    for domain_name, status in results:
        if status == "AVAILABLE":
            print(f"{domain_name}: {status}")

    return 0


if __name__ == '__main__':
    exit(main())
