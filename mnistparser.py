class MNISTParser:

    def __init__(self, label_filename, image_filename):
        self.label_generator = bytes_from_file(label_filename)
        self.image_generator = bytes_from_file(image_filename)

        # Not sure if the magic numbers serve a purpose. Doesn't really look like it.
        # But they're defined in the definition of the data set. So.. there they are.
        self.label_magic_number = 0
        self.label_num_items = 0

        self.image_magic_number = 0
        self.image_num_items = 0
        self.image_rows = 0
        self.image_cols = 0

        # The repeated loops are a bit messy, but work. The metadata which precedes the labels and image
        # files is read, and each generator is then put in the correct position to begin reading data
        for i in range(4):
            self.label_magic_number = append_byte(self.label_magic_number, ord(self.label_generator.next()))
        for i in range(4):
            self.label_num_items = append_byte(self.label_num_items, ord(self.label_generator.next()))

        for i in range(4):
            self.image_magic_number = append_byte(self.image_magic_number, ord(self.image_generator.next()))
        for i in range(4):
            self.image_num_items = append_byte(self.image_num_items, ord(self.image_generator.next()))
        for i in range(4):
            self.image_rows = append_byte(self.image_rows, ord(self.image_generator.next()))
        for i in range(4):
            self.image_cols = append_byte(self.image_cols, ord(self.image_generator.next()))
        # Sanity check
        assert self.label_num_items == self.image_num_items

    def __iter__(self):
        return self

    def next(self):
        try:
            label = ord(self.label_generator.next())
            image = []
            for i in range(0, self.image_rows * self.image_cols):
                image.append(ord(self.image_generator.next()))
            return MNISTElement(label, image)
        except StopIteration:
            # Signals that the generator is out of elements and the iterator should quit too
            # Seems like an odd way to do that. Maybe it's ok.
            raise StopIteration


class MNISTElement:

    def __init__(self, label, image=[]):
        self.label = label
        self.image = image


def append_byte(num, byte):
    return (num << 8) | byte

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break
