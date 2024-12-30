class HelperFuncs:
    def __init__(self):
        self.count_start = False

    def start_timer(self, seconds, label, root, to_clear, paragraph, render):
        if not self.count_start:
            self.count_start = True
            self.count_down(seconds, label, root, to_clear, paragraph, render)

    def compare(self, typed_words, paragraph, func):
        typed_list = typed_words.split()
        paragraph_list = paragraph.split()
        typos = 0
        correct_words = 0

        for i in range(len(typed_list)):
            if typed_list[i] == paragraph_list[i]:
                correct_words += 1
            else:
                typos += 1

        func(len(typed_list), correct_words, typos)

    def update_label(self, label, minutes, seconds):
        label.config(text=f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    def new_window(self, to_clear):
        for widget in to_clear:
            widget.destroy()

    def count_down(self, seconds, label, root, to_clear, paragraph, render):
        mins, sec = divmod(seconds, 60)

        if seconds > 0:
            self.update_label(label, mins, sec)
            seconds -= 1
            root.after(
                1000,
                lambda: self.count_down(
                    seconds, label, root, to_clear, paragraph, render
                ),
            )
        else:
            self.compare(to_clear[2].get(), paragraph, render)
            self.new_window(to_clear)
