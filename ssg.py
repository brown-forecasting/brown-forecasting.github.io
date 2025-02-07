from jinja2 import Environment, FileSystemLoader
import os
import shutil

def build_site():
    # Create output directory if it doesn't exist
    output_dir = 'docs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Copy assets directory if it exists
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        output_assets_dir = os.path.join(output_dir, 'assets')
        if os.path.exists(output_assets_dir):
            shutil.rmtree(output_assets_dir)
        shutil.copytree(assets_dir, output_assets_dir)
        print('Copied assets directory')

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # List of pages to generate
    pages = ['index.html', 'about.html', 'schedule.html', "tournament.html"]

    # Generate each page
    for page in pages:
        template = env.get_template(page)
        output = template.render()
        
        # Write to output file
        with open(os.path.join(output_dir, page), 'w', encoding='utf-8') as f:
            f.write(output)
        print(f'Generated {page}')

if __name__ == '__main__':
    build_site()
