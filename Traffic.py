import time
while True:
    print("\n===== TRAFFIC SIGNAL =====")
    print("RED---STOP")
    time.sleep(3)
    print("YELLOW---READY")
    time.sleep(2)
    print("GREEN---GO")
    time.sleep(5)
    print("Signal cycle completed!")
    choice=input("Continue signal?(yes/no): ")
    if choice.lower()=="no":
        print("Traffic signal stopped.")
        break
