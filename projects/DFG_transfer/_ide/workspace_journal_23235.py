# 2025-12-22T20:48:16.199229
import vitis

client = vitis.create_client()
client.set_workspace(path="DFG_transfer")

comp = client.get_component(name="dfg_0")
comp.run(operation="C_SIMULATION")

comp.run(operation="SYNTHESIS")

vitis.dispose()

