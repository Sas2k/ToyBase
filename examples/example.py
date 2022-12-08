from ToyBase import ToyBase

base = ToyBase.ToyBase("test")

base.create_table(["Name", "Age"])

base.add_record(["John", 20])

print(base.show_records())

print(base.get_record(0))

base.delete_record(0)

print(base.show_records())

print(str(base))