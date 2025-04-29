# # import serial

# # ser = serial.Serial('/dev/ttyUSB0', 9600)
# # while True:
# #     line = ser.readline().decode('utf-8')
# #     if line.startswith('$GPGGA'):  # NMEA sentence for location
# #         print(line)


# import geocoder

# g = geocoder.ip('me')
# print("Latitude:", g.latlng[0])
# print("Longitude:", g.latlng[1])
