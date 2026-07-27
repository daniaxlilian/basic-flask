from flask import Flask, render_template

app = Flask(__name__)

house_colours = {"artemis": "green",
                 "helios": "red",
                 "athena": "purple",
                 "poseidon": "blue"
                }

house_points = {"artemis": "3456",
                 "helios": "6767",
                 "athena": "90",
                 "poseidon": "-10549"
                }

visited_houses = []

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/<text>")
def info(text):
    if text in house_colours.keys():
        house = text
        house_colour = house_colours[text]
        house_pt = house_points[text]
        if house not in visited_houses:
            visited_houses.append(house)
        return render_template("index.html", house=house, house_colour=house_colour, house_pt=house_pt)

    else:
        num_digits = 0
        num_vowels = 0
        num_cons = 0
        char_dict = {}

        length = len(text)

        for char in text:
            if char.isdigit():
                num_digits += 1

            elif char.isalpha():
                if char in "aeiouAEIOU":
                    num_vowels += 1
                else:
                    num_cons += 1

            if char not in char_dict.keys():
                char_dict[char] = 1
            else:
                char_dict[char] += 1


            if "67" in text:
                bgc = "pink"
            else:
                bgc = "black"

        
        return render_template("analyse.html",
                               bgc=bgc,
                               char_dict=char_dict,
                               text=text,
                               length=length,
                               num_digits=num_digits,
                               num_vowels=num_vowels,
                               num_cons=num_cons)
                
        
if __name__ == "__main__":
    app.run(port=2525)
    
