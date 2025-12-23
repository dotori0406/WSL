# 2025-12-22T17:52:34.522318
import vitis

client = vitis.create_client()
client.set_workspace(path="DFG_transfer")

comp = client.create_hls_component(name = "dfg_0",cfg_file = ["hls_config.cfg"],template = "empty_hls_component")

vitis.dispose()

