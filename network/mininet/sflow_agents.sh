ovs-vsctl -- --id=@sflow create sflow agent=eth0  target=\"10.0.1.16:6343\" sampling=10 polling=20 -- -- set bridge s1 sflow=@sflow
ovs-vsctl -- --id=@sflow create sflow agent=eth0  target=\"10.0.1.16:6343\" sampling=10 polling=20 -- -- set bridge s2 sflow=@sflow
ovs-vsctl -- --id=@sflow create sflow agent=eth0  target=\"10.0.1.16:6343\" sampling=10 polling=20 -- -- set bridge s3 sflow=@sflow
