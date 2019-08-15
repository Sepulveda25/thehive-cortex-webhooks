/////////// Lo que recibe TheHive

#{"artifacts":[{"data":"172.22.71.200","dataType":"source_ip","message":null,"tags":[],"tlp":2},{"data":"200.16.16.170","dataType":"destination_ip","message":null,"tags":[],"tlp":2},{"data":"49390","dataType":"source_port","message":null,"tags":[],"tlp":2},{"data":"80","dataType":"destination_port","message":null,"tags":[],"tlp":2},{"data":"sonion-virtual-machine-ens192","dataType":"interface","message":null,"tags":[],"tlp":2},{"data":"2019-07-29T17:22:23.387Z","dataType":"timestamp","message":null,"tags":[],"tlp":2},{"data":"snort","dataType":"event_type","message":null,"tags":[],"tlp":2}],"caseTemplate":null,"customFields":{},"date":1564421041000,"description":"[1:2022913:3] Web Application Attack ET INFO WinHttp AutoProxy Request wpad.dat Possible BadTunnel [Classification: Generic Protocol Command Decode] [Priority: 3]: <sonion-virtual-machine-ens192> {TCP} 172.22.71.200:49390 -> 200.16.16.170:80","severity":3,"source":"SecurityOnion","sourceRef":"c9ea09","tags":["elastalert, SecurityOnion, info"],"title":"New IDS Alert! -- ET INFO WinHttp AutoProxy Request wpad.dat Possible BadTunnel ","tlp":3,"type":"external"}

//////////// Lo que thehive le manda a cortex


#{"label":"[SecurityOnion:3e74f5] New IDS Alert! -- ET INFO WinHttp AutoProxy Request wpad.dat Possible BadTunnel ","data":{"severity":3,"date":1564421060000,"_routing":"24ee7208979d7cd293e3e383721333ba","customFields":{},"caseTemplate":null,"_type":"alert","description":"[1:2022913:3] ET INFO WinHttp AutoProxy Request wpad.dat Possible BadTunnel [Classification: Generic Protocol Command Decode] [Priority: 3]: <sonion-virtual-machine-ens192> {TCP} 172.22.71.200:49390 -> 200.16.16.170:80","lastSyncDate":1564421055957,"source":"SecurityOnion","type":"external","follow":true,"title":"New IDS Alert! -- ET INFO WinHttp AutoProxy Request wpad.dat Possible BadTunnel ","tags":["elastalert, SecurityOnion, info"],"createdAt":1564421055956,"_parent":null,"createdBy":"eco","tlp":3,"_id":"24ee7208979d7cd293e3e383721333ba","id":"24ee7208979d7cd293e3e383721333ba","sourceRef":"3e74f5","_version":1,"status":"New","artifacts":[{"data":"172.22.71.200","dataType":"source_ip","message":null,"tags":[],"tlp":2},{"data":"200.16.16.170","dataType":"destination_ip","message":null,"tags":[],"tlp":2},{"data":"49390","dataType":"source_port","message":null,"tags":[],"tlp":2},{"data":"80","dataType":"destination_port","message":null,"tags":[],"tlp":2},{"data":"sonion-virtual-machine-ens192","dataType":"interface","message":null,"tags":[],"tlp":2},{"data":"2019-07-29T17:22:23.475Z","dataType":"timestamp","message":null,"tags":[],"tlp":2},{"data":"snort","dataType":"event_type","message":null,"tags":[],"tlp":2}]},"dataType":"thehive:alert","tlp":2,"pap":2,"message":"","parameters":{"user":"thehive"}}

