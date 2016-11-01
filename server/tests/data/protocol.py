from opentrons import containers
from opentrons import instruments

plate = containers.load(
    '96-flat',
    'A2',
    'plate'
)

tiprack = containers.load(
    'tiprack-10ul',
    'A1',
    'tiprack'
)

trash = containers.load(
    'point',
    'B2',
    'trash'
)

p10 = instruments.Pipette(
    name="p10",
    trash_container=trash,
    tip_racks=[tiprack],
    min_volume=1,
    axis="b",
    channels=1
)

p10.set_max_volume(10)
p10.pick_up_tip()
p10.aspirate(5, plate[0]).dispense(5, plate[1]).mix(5)
p10.aspirate(5, plate[1]).dispense(5, plate[1]).mix(5)
p10.aspirate(5, plate[2]).dispense(5, plate[1]).mix(5)
p10.aspirate(5, plate[3]).dispense(5, plate[1]).mix(5)
p10.drop_tip()
