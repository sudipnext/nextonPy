from itemadapter import ItemAdapter
import re

class GajabkoPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        
        for field_name in field_names:
            value = adapter.get(field_name)
            if field_name != 'description':
                if value is not None:
                    if isinstance(value, str):
                        adapter[field_name] = value.strip()
                        if field_name == 'description':
                            # Remove extra spaces between "Model:" and the model number
                            adapter[field_name] = [line.strip().replace("Model: ", "Model:") for line in value]
                            # Remove extra spaces between "Technical Specification:" and its values
                            adapter[field_name] = [re.sub(r'\s*:\s*', ':', line) for line in adapter[field_name]]
                        elif field_name == 'price':
                            # Convert price to float
                            adapter[field_name] = float(value.strip())
                    elif isinstance(value, list):
                        stripped_values = [v.strip() if isinstance(v, str) else v for v in value]
                        adapter[field_name] = stripped_values
                    
            elif field_name == 'description':
                adapter[field_name] = [re.sub(r'\s+', ' ', line.strip()) for line in value]
        
        return item
