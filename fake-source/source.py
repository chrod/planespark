#!/usr/bin/python2

import time
import datetime

import SocketServer

class SBSTcpHandler(SocketServer.StreamRequestHandler):
    def handle(self):
	while True:
		now = datetime.datetime.now()
		thedate = now.strftime("%Y/%m/%d")
		thetime = now.strftime("%H:%M:%S.000")

		s = """SEL,,496,2286,4CA4E5,27215,$THEDATE,$THETIME,$THEDATE,$THETIME,RYR1427
ID,,496,7162,405637,27928,$THEDATE,$THETIME,$THEDATE,$THETIME,EZY691A
AIR,,496,5906,400F01,27931,$THEDATE,$THETIME,$THEDATE,$THETIME
STA,,5,179,400AE7,10103,$THEDATE,$THETIME,$THEDATE,$THETIME,RM
CLK,,496,-1,,-1,$THEDATE,$THETIME,$THEDATE,$THETIME
MSG,1,145,256,7404F2,11267,$THEDATE,$THETIME,$THEDATE,$THETIME,RJA1118,,,,,,,,,,,
MSG,2,496,603,400CB6,13168,$THEDATE,$THETIME,$THEDATE,$THETIME,,,0,76.4,258.3,54.05735,-4.38826,,,,,,0
MSG,3,496,211,4CA2D6,10057,$THEDATE,$THETIME,$THEDATE,$THETIME,,37000,,,51.45735,-1.02826,,,0,0,0,0
MSG,4,496,469,4CA767,27854,$THEDATE,$THETIME,$THEDATE,$THETIME,,,288.6,103.2,,,-832,,,,,
MSG,5,496,329,394A65,27868,$THEDATE,$THETIME,$THEDATE,$THETIME,,10000,,,,,,,0,,0,0
MSG,6,496,237,4CA215,27864,$THEDATE,$THETIME,$THEDATE,$THETIME,,33325,,,,,,0271,0,0,0,0
MSG,7,496,742,51106E,27929,$THEDATE,$THETIME,$THEDATE,$THETIME,,3775,,,,,,,,,,0
MSG,8,496,194,405F4E,27884,$THEDATE,$THETIME,$THEDATE,$THETIME,,,,,,,,,,,,0
""".replace('$THEDATE', thedate).replace('$THETIME', thetime)
		self.wfile.write(s)
		time.sleep(5)


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 30003
    server = SocketServer.TCPServer((HOST, PORT), SBSTcpHandler)
    server.serve_forever()