#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System()
    await drone.connect(system_address="serial:///dev/ttyACM0")

    print("-- Starting gyroscope calibration")
    async for progress_data in drone.calibration.calibrate_gyro():
        print(progress_data)
    print("-- Gyroscope calibration finished")


 


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
