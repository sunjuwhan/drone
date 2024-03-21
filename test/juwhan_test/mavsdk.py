import asyncio
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyAMA0:57600")

    print("Waiting for drone to become ready...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    async for health in drone.telemetry.health():
        if health.is_gyrometer_calibration_ok and health.is_accelerometer_calibration_ok and health.is_magnetometer_calibration_ok and health.is_barometer_calibration_ok:
            print("Drone is ready.")
            break

    print("Arming drone...")
    await drone.action.arm()

    async for arming_info in drone.telemetry.armed():
        if arming_info.is_armed:
            print("Drone is armed.")
            break

    print("End of script.")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
