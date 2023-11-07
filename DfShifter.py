

class DataFrameShifter:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def shift_data(self, columns, shift_values):
        self.data_frame2 = self.data_frame.copy()
        try:
            if len(columns) != len(shift_values):
                raise ValueError("The number of columns and shift values must be the same.")

            for col, shift in zip(columns, shift_values):
                # Get the column name or index based on user input
                if isinstance(col, int):
                    column_name = self.data_frame.columns[col]
                elif col in self.data_frame.columns:
                    column_name = col
                else:
                    raise ValueError("Column not found in the DataFrame.")

                # Shift the data in the specified column by the given shift value
                
                self.data_frame2[column_name] = self.data_frame2[column_name].shift(shift)

            return self.data_frame2
        except Exception as e:
            return str(e)