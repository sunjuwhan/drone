from mavsdk import System
import asyncio

async def connect_drone():
    
    
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyAMA0:57600")
    return drone


async def arm_drone(drone):
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


async def main():
    drone = await connect_drone()
    await arm_drone(drone)
    print("End of script.")


if __name__ == "__main__":
    asyncio.run(main())
