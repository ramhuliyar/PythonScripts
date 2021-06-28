import re

psbOutILer = """
PSB: 
 P2P: Session (To: 42.1.1.1 - 1 - 40.1.1.1), Sender (40.1.1.1 - 25092) PHop 0.0.0.0

 PSB CurrState: PRIMARYS_CONNECTED  PrevState: PRIMARYS_INIT  Flags: 0x0
 LocalLabel 0 OutLabel 524287
 Incoming IfIndex: Interface: Local API(-1)
 Refresh interval 30, Send Path refresh in 28 secs,  Path Refresh timeout 0 secs
 PrevHop: Ctype 1  Addr 0.0.0.0, LIH 0
 DnStream Nbr: Addr-> 10.1.1.2  IfIndex to-41(2)
 UpStream Neighbor is NULLP
 Session Attribute:
   Session Name: to-42::to-42
   HoldPri: 0 SetupPri: 7 Flags: 0x6
   Ctype: 7, IncludeGroup: 0x0 IncludeAllGroup: 0x0 ExcludeGroup: 0x0
 ClassType: Absent
 TSpec: Flags 0x8000 QOSC 1, PDR (infinity), PBS 0.000 bps, CDR (0.000 bps) MTU: 0 <<<<<<
 PSB RRO : -> 
  (1) * Flags : 0x0 :      I 
  (1) * IPv4 -> 10.1.1.1(40.1.1.1)
 PSB SENT RRO : ->
"""

psbOutTransit = """
PSB: 
 P2P: Session (To: 42.1.1.1 - 1 - 40.1.1.1), Sender (40.1.1.1 - 25092) PHop 10.1.1.1

 PSB CurrState: PRIMARYS_CONNECTED  PrevState: PRIMARYS_INIT  Flags: 0x0
 LocalLabel 524287 OutLabel 524287
 Incoming IfIndex: to-40(2)
 Refresh interval 30, Send Path refresh in 3 secs,  Path Refresh timeout 136 secs
 Send Resv refresh in 24 secs
 PrevHop: Ctype 1  Addr 10.1.1.1, LIH 2
 DnStream Nbr: Addr-> 11.1.1.2  IfIndex to-42(3)
 UpStream Nbr: Addr-> 10.1.1.1  IfIndex to-40(2)
 Session Attribute:
   Session Name: to-42::to-42
   HoldPri: 0 SetupPri: 7 Flags: 0x6
   Ctype: 7, IncludeGroup: 0x0 IncludeAllGroup: 0x0 ExcludeGroup: 0x0
 ClassType: Absent
 TSpec: Flags 0x8000 QOSC 1, PDR (infinity), PBS 0.000 bps, CDR (0.000 bps) MTU: 9198
 PSB RRO : -> 
"""

for psbOut in [psbOutILer, psbOutTransit]:
    psbOutLines = psbOut.split('\n')
    for index, line in enumerate(psbOutLines):
        match = re.search('LocalLabel\s+(?P<OutLabel>\d+)', line,re.I)
        if match:
            print(match.group('OutLabel'))
        
