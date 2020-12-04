from Mac import MAC_Changer

if __name__ == "__main__":
    mc = MAC_Changer()
    #print(mc.get_MAC("eth0"))
    mc.change_mac("eth0","01:23:45:67:89:99")