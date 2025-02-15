def validate_can(can):
	""" DbC checks for required can fields and settings
	returns False if can is valid
	returns a string describing the error otherwise
	"""
	try:
		#Test id
		can["id"] = int(can["id"])
		if can["id"] < 0 or 999999999 < can["id"]:
            raise ValueError("can.id out of range [0..999999999]")
        if can["deployed"] == "True":
            can["deployed"] = True
        elif can["deployed"] == "False":
            can["deployed"] = False
        else:
            raise ValueError("can.deployed must be Boolean (True, False)")
        #Test capacity
        can["capacity"] = float(can["capacity"])
        if can["capacity"] <= 0.0 or 9999 < can["capacity"]:
            raise ValueError("can.capacity out of range (0.0..9999.0]")
    #Test lat
        can["lat"] = float(can["lat"])
        if can["lat"] < -90.0 or 90.0 < can["lat"]:
            raise ValueError("can.lat out of range [-90.0..90.0]")
#Test lon
        can["lon"] = float(can["lon"])
        if can["lon"] < -180.0 or 180.0 < can["lon"]:
            raise ValueError("can.lon out of range [-180.0..180.0]")
    #Test power
        if "power" not in can:
            raise ValueError("field 'power' must be present")
	except Exception as ex:
		return str(ex)
	return "" #no errors