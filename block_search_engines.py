import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c",
        "--choices",
        help="Program type",
        metavar="<iptables/ufw>",
        required=True,
        dest="choices",
        type=str,
        choices=["iptables", "ufw"],
    )

    args = parser.parse_args()

    if args.choices == "iptables":
        block = "sudo iptables -A INPUT -s {} -j DROP"
    elif args.choices == "ufw":
        block = "sudo ufw deny from {} to any"

    ips = [
        #Shodan
    "208.180.20.97",
    "198.20.69.74",
    "198.20.69.98",
    "198.20.70.114",
    "198.20.99.130",
    "93.120.27.62",
    "66.240.236.119",
    "71.6.135.131",
    "66.240.192.138",
    "71.6.167.142",
    "82.221.105.6",
    "82.221.105.7",
    "71.6.165.200",
    "188.138.9.50",
    "85.25.103.50",
    "85.25.43.94",
    "71.6.146.185",
    "71.6.158.166",
    "198.20.87.98",
    "66.240.219.146",
    "209.126.110.38",
    "104.236.198.48",
    "104.131.0.69",
    "162.159.244.38",
    "93.174.95.106",
    "94.102.49.193",
    "80.82.77.139",
    "94.102.49.190",
    "185.163.109.66",
    "89.248.172.16",
    "71.6.146.186",
    "89.248.167.131",
    "159.203.176.62",
    "185.181.102.18",
    "80.82.77.33",
    "216.117.2.180",
    "71.6.199.23",
    "185.142.236.34",
    "185.165.190.34",
    "71.6.135.131",
    "185.142.236.35",
    "66.240.219.133",
    "143.198.225.197",
    "137.184.95.216",
    "64.227.90.185",
    "143.198.238.87",
    "137.184.190.205",
    "137.184.112.192",
    "137.184.190.188",
    "167.172.219.157",
    "143.110.239.2",
    "143.198.68.20",
    "137.184.190.194",
    "137.184.190.246",
    "137.184.9.17",
    "137.184.13.100",
    "137.184.94.133",
    "137.184.112.103",
    "137.184.180.190",
    "143.198.50.234",
    "185.142.236.36",
    "185.142.236.40",
    "185.142.236.41",
    "185.142.236.43",
    "185.142.239.16",
    "198.20.69.96/29",
    "198.20.70.112/29",
    "198.20.87.96/29",
    "198.20.99.128/29",
    "66.240.205.34",
    "71.6.146.130",
    "71.6.147.198",
    "71.6.147.254",
    "71.6.150.153",
    "71.6.167.125",
    "89.248.172.7",
        #Censys
    "162.142.125.0/24",
    "167.94.138.0/24",
    "167.94.145.0/24",
    "167.94.146.0/24",
    "167.248.133.0/24",
    "2602:80d:1000:b0cc:e::/80",
    "2620:96:e000:b0cc:e::/80",
    ]

    for i in ips:
        subprocess.run(block.format(i), shell=True)

if __name__ == "__main__":
    main()
