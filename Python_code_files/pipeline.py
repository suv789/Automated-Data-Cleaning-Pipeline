
class DataCleaningPipeline:

    """
    A modular pipeline for cleaning data with customizable steps.
    """

    def __init__(self):
        self.steps = []

    def add_step(self, name, function):
        """Add a cleaning step."""
        self.steps.append({'name': name, 'function': function})

    def execute(self,df):
        "Execute all cleaning step in order"
        results = []
        current_df = df.copy()

        for step in self.steps:
            try:
                current_df = step['function'](current_df)
                results.append({'step': step['name'], 'status': 'success', 'rows_affected': len(current_df)})
            except Exception as e:
                  
                  results.append({'step': step['name'], 'status': 'failed', 'error': str(e)})
                  break
        
        return current_df,results