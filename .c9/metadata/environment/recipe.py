{"filter":false,"title":"recipe.py","tooltip":"/recipe.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":25,"column":44},"end":{"row":25,"column":45},"action":"insert","lines":["\""],"id":117}],[{"start":{"row":22,"column":0},"end":{"row":25,"column":46},"action":"remove","lines":["@app.route('/add_recipes')","def add_recipes():","    from_scratch = mongo.db.myRecipes.find()","    return render_template( \"addrecipes.html\")"],"id":118}],[{"start":{"row":15,"column":15},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":119},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":120}],[{"start":{"row":17,"column":0},"end":{"row":20,"column":46},"action":"insert","lines":["@app.route('/add_recipes')","def add_recipes():","    from_scratch = mongo.db.myRecipes.find()","    return render_template( \"addrecipes.html\")"],"id":121}],[{"start":{"row":26,"column":71},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":122}],[{"start":{"row":26,"column":71},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":123},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":4},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":124}],[{"start":{"row":28,"column":0},"end":{"row":32,"column":41},"action":"insert","lines":["@app.route('/insert_task', methods=['POST'])","def insert_task():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_tasks'))"],"id":125}],[{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"remove","lines":["k"],"id":126},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"remove","lines":["s"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"remove","lines":["a"]},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"remove","lines":["t"]}],[{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["r"],"id":127},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["e"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["c"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["i"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["p"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"remove","lines":["k"],"id":128},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"remove","lines":["s"]},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"remove","lines":["a"]},{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"remove","lines":["t"]}],[{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["r"],"id":129},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["e"]},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["c"]},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["i"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["p"]},{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"remove","lines":["s"],"id":130},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["k"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["s"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["a"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["f"],"id":131},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["r"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["o"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["m"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"insert","lines":["s"],"id":132},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":["c"]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["r"]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["a"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["t"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"insert","lines":["c"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"insert","lines":["h"]}],[{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["s"],"id":133},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["k"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"remove","lines":["s"]},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"remove","lines":["a"]},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"insert","lines":["m"],"id":134},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"insert","lines":["y"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"insert","lines":["R"]},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"insert","lines":["c"],"id":135},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"insert","lines":["i"]},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"insert","lines":["p"]}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":["e"],"id":136},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"insert","lines":["s"]}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"remove","lines":["s"],"id":137},{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"remove","lines":["k"]},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"remove","lines":["s"]},{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"remove","lines":["a"]},{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["r"],"id":138},{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"insert","lines":["e"]},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"insert","lines":["c"]},{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":["i"]},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["p"]},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":37},"end":{"row":32,"column":38},"action":"remove","lines":["s"],"id":139},{"start":{"row":32,"column":36},"end":{"row":32,"column":37},"action":"remove","lines":["k"]},{"start":{"row":32,"column":35},"end":{"row":32,"column":36},"action":"remove","lines":["s"]},{"start":{"row":32,"column":34},"end":{"row":32,"column":35},"action":"remove","lines":["a"]},{"start":{"row":32,"column":33},"end":{"row":32,"column":34},"action":"remove","lines":["t"]}],[{"start":{"row":32,"column":33},"end":{"row":32,"column":34},"action":"insert","lines":["t"],"id":140}],[{"start":{"row":32,"column":33},"end":{"row":32,"column":34},"action":"remove","lines":["t"],"id":141}],[{"start":{"row":32,"column":33},"end":{"row":32,"column":34},"action":"insert","lines":["r"],"id":142},{"start":{"row":32,"column":34},"end":{"row":32,"column":35},"action":"insert","lines":["e"]},{"start":{"row":32,"column":35},"end":{"row":32,"column":36},"action":"insert","lines":["c"]},{"start":{"row":32,"column":36},"end":{"row":32,"column":37},"action":"insert","lines":["i"]},{"start":{"row":32,"column":37},"end":{"row":32,"column":38},"action":"insert","lines":["p"]},{"start":{"row":32,"column":38},"end":{"row":32,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":39},"end":{"row":32,"column":40},"action":"insert","lines":["s"],"id":143}],[{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["s"],"id":144}],[{"start":{"row":28,"column":42},"end":{"row":28,"column":43},"action":"remove","lines":["T"],"id":145},{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"remove","lines":["S"]},{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"remove","lines":["O"]},{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"remove","lines":["P"]}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":[","],"id":146}],[{"start":{"row":28,"column":0},"end":{"row":32,"column":43},"action":"remove","lines":["@app.route('/insert_recipe', methods=[','])","def insert_recipe():","    from_scratch = mongo.db.myRecipes","    recipes.insert_one(request.form.to_dict())","    return redirect(url_for('get_recipes'))"],"id":147}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"remove","lines":["R"],"id":148},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"remove","lines":["y"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"remove","lines":["m"]}],[{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["r"],"id":149}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":150},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":21,"column":71},"action":"insert","lines":["@app.route('/get_recipes')","#Display text as proof of concept","def get_recipes():","    from_scratch = mongo.db.recipes.find()","    return render_template( \"recipes.html\", from_scratch=from_scratch) "],"id":151}],[{"start":{"row":28,"column":0},"end":{"row":32,"column":70},"action":"remove","lines":["@app.route('/get_recipes')","#Display text as proof of concept","def get_recipes():","    from_scratch = mongo.db.recipes.find()","    return render_template( \"recipes.html\", from_scratch=from_scratch)"],"id":152}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["d"],"id":153},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["d"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["",""],"id":154},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"remove","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]},{"start":{"row":28,"column":1},"end":{"row":29,"column":0},"action":"remove","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":[" "]},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":26,"column":43},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":155}],[{"start":{"row":26,"column":43},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":156},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":4},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":157}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["@"],"id":158},{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"insert","lines":["a"]},{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"insert","lines":["p"]},{"start":{"row":28,"column":3},"end":{"row":28,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["."],"id":159},{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"insert","lines":["r"]},{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"insert","lines":["u"],"id":160},{"start":{"row":28,"column":8},"end":{"row":28,"column":9},"action":"insert","lines":["t"]},{"start":{"row":28,"column":9},"end":{"row":28,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":28,"column":10},"end":{"row":28,"column":12},"action":"insert","lines":["()"],"id":161}],[{"start":{"row":28,"column":11},"end":{"row":28,"column":13},"action":"insert","lines":["''"],"id":162}],[{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["/"],"id":163},{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["i"]},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["n"]},{"start":{"row":28,"column":15},"end":{"row":28,"column":16},"action":"insert","lines":["s"]},{"start":{"row":28,"column":16},"end":{"row":28,"column":17},"action":"insert","lines":["e"]},{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"insert","lines":["r"]},{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["_"],"id":164},{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["r"]},{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["e"]},{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["c"]},{"start":{"row":28,"column":23},"end":{"row":28,"column":24},"action":"insert","lines":["i"]},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"insert","lines":["p"]},{"start":{"row":28,"column":25},"end":{"row":28,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":28,"column":28},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":165},{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["d"]},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"insert","lines":["e"]},{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":29,"column":3},"end":{"row":29,"column":4},"action":"insert","lines":[" "],"id":166},{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["i"]},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["n"]},{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["s"]}],[{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["e"],"id":167},{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["r"]},{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["t"]},{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["_"]}],[{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["r"],"id":168},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["e"]},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["c"]},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["i"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["p"]}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["e"],"id":169}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":19},"action":"insert","lines":["()"],"id":170}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":[":"],"id":171}],[{"start":{"row":29,"column":20},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":172},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":[","],"id":173}],[{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"insert","lines":[" "],"id":174},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"insert","lines":["m"]},{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"insert","lines":["e"]},{"start":{"row":28,"column":31},"end":{"row":28,"column":32},"action":"insert","lines":["t"]},{"start":{"row":28,"column":32},"end":{"row":28,"column":33},"action":"insert","lines":["h"]},{"start":{"row":28,"column":33},"end":{"row":28,"column":34},"action":"insert","lines":["o"]},{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"insert","lines":["g"]}],[{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"remove","lines":["g"],"id":175}],[{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"insert","lines":["d"],"id":176}],[{"start":{"row":28,"column":35},"end":{"row":28,"column":36},"action":"insert","lines":["s"],"id":177},{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":["="]}],[{"start":{"row":28,"column":37},"end":{"row":28,"column":39},"action":"insert","lines":["[]"],"id":178}],[{"start":{"row":28,"column":38},"end":{"row":28,"column":40},"action":"insert","lines":["''"],"id":179}],[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":["G"],"id":180},{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"insert","lines":["E"]},{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"insert","lines":["T"]}],[{"start":{"row":28,"column":43},"end":{"row":28,"column":44},"action":"insert","lines":[","],"id":181}],[{"start":{"row":28,"column":44},"end":{"row":28,"column":46},"action":"insert","lines":["''"],"id":182}],[{"start":{"row":28,"column":45},"end":{"row":28,"column":46},"action":"insert","lines":["P"],"id":183},{"start":{"row":28,"column":46},"end":{"row":28,"column":47},"action":"insert","lines":["O"]},{"start":{"row":28,"column":47},"end":{"row":28,"column":48},"action":"insert","lines":["S"]},{"start":{"row":28,"column":48},"end":{"row":28,"column":49},"action":"insert","lines":["T"]}],[{"start":{"row":29,"column":20},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":184},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["t"],"id":185},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["a"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["s"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["k"]}],[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"remove","lines":["k"],"id":186},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"remove","lines":["s"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"remove","lines":["a"]},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":42},"action":"insert","lines":["from_scratch = mongo.db.recipes.find()"],"id":187}],[{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"remove","lines":[")"],"id":188},{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"remove","lines":["("]},{"start":{"row":30,"column":39},"end":{"row":30,"column":40},"action":"remove","lines":["d"]},{"start":{"row":30,"column":38},"end":{"row":30,"column":39},"action":"remove","lines":["n"]},{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"remove","lines":["i"]},{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"remove","lines":["f"]},{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["."]}],[{"start":{"row":30,"column":35},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":189},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["f"],"id":190},{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"insert","lines":["r"]},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"insert","lines":["o"]},{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":["_"],"id":191},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["s"]},{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":["c"]},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["r"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":["a"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["t"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["c"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["h"]}],[{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["_"],"id":192}],[{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"remove","lines":["_"],"id":193}],[{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["."],"id":194},{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["i"]},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["n"]},{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["s"]},{"start":{"row":31,"column":20},"end":{"row":31,"column":21},"action":"insert","lines":["e"]},{"start":{"row":31,"column":21},"end":{"row":31,"column":22},"action":"insert","lines":["r"]},{"start":{"row":31,"column":22},"end":{"row":31,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":23},"end":{"row":31,"column":24},"action":"insert","lines":["_"],"id":195},{"start":{"row":31,"column":24},"end":{"row":31,"column":25},"action":"insert","lines":["o"]},{"start":{"row":31,"column":25},"end":{"row":31,"column":26},"action":"insert","lines":["n"]},{"start":{"row":31,"column":26},"end":{"row":31,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":27},"end":{"row":31,"column":29},"action":"insert","lines":["()"],"id":196}],[{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"insert","lines":["r"],"id":197},{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"insert","lines":["e"]},{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["q"]},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["u"]},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["e"]},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"remove","lines":["t"],"id":198}],[{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["s"],"id":199},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"insert","lines":["t"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"insert","lines":["."]},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"insert","lines":["f"]}],[{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"insert","lines":["o"],"id":200},{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["r"]},{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["m"]},{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"insert","lines":["."]},{"start":{"row":31,"column":41},"end":{"row":31,"column":42},"action":"insert","lines":["t"]},{"start":{"row":31,"column":42},"end":{"row":31,"column":43},"action":"insert","lines":["o"]}],[{"start":{"row":31,"column":43},"end":{"row":31,"column":44},"action":"insert","lines":["_"],"id":201},{"start":{"row":31,"column":44},"end":{"row":31,"column":45},"action":"insert","lines":["d"]},{"start":{"row":31,"column":45},"end":{"row":31,"column":46},"action":"insert","lines":["i"]},{"start":{"row":31,"column":46},"end":{"row":31,"column":47},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":46},"end":{"row":31,"column":47},"action":"remove","lines":["t"],"id":202}],[{"start":{"row":31,"column":46},"end":{"row":31,"column":47},"action":"insert","lines":["c"],"id":203},{"start":{"row":31,"column":47},"end":{"row":31,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":48},"end":{"row":31,"column":50},"action":"insert","lines":["()"],"id":204}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["r"],"id":205},{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"insert","lines":["e"]},{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["t"]},{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"insert","lines":["u"]},{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["r"]},{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":[" "],"id":206},{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"insert","lines":["r"]},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"insert","lines":["e"]},{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":["d"]},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["i"]},{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":["r"]},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"insert","lines":["e"]},{"start":{"row":32,"column":17},"end":{"row":32,"column":18},"action":"insert","lines":["c"]},{"start":{"row":32,"column":18},"end":{"row":32,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":19},"end":{"row":32,"column":21},"action":"insert","lines":["()"],"id":207}],[{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"insert","lines":["u"],"id":208},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"insert","lines":["r"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"insert","lines":["l"]}],[{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"insert","lines":["_"],"id":209},{"start":{"row":32,"column":24},"end":{"row":32,"column":25},"action":"insert","lines":["f"]},{"start":{"row":32,"column":25},"end":{"row":32,"column":26},"action":"insert","lines":["o"]},{"start":{"row":32,"column":26},"end":{"row":32,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":32,"column":27},"end":{"row":32,"column":29},"action":"insert","lines":["()"],"id":210}],[{"start":{"row":32,"column":28},"end":{"row":32,"column":30},"action":"insert","lines":["''"],"id":211}],[{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"insert","lines":["g"],"id":212},{"start":{"row":32,"column":30},"end":{"row":32,"column":31},"action":"insert","lines":["e"]},{"start":{"row":32,"column":31},"end":{"row":32,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":31},"end":{"row":32,"column":32},"action":"remove","lines":["t"],"id":213},{"start":{"row":32,"column":30},"end":{"row":32,"column":31},"action":"remove","lines":["e"]},{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"remove","lines":["g"]}],[{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"insert","lines":["g"],"id":214},{"start":{"row":32,"column":30},"end":{"row":32,"column":31},"action":"insert","lines":["e"]},{"start":{"row":32,"column":31},"end":{"row":32,"column":32},"action":"insert","lines":["t"]},{"start":{"row":32,"column":32},"end":{"row":32,"column":33},"action":"insert","lines":["_"]}],[{"start":{"row":32,"column":33},"end":{"row":32,"column":34},"action":"insert","lines":["r"],"id":215},{"start":{"row":32,"column":34},"end":{"row":32,"column":35},"action":"insert","lines":["e"]},{"start":{"row":32,"column":35},"end":{"row":32,"column":36},"action":"insert","lines":["c"]},{"start":{"row":32,"column":36},"end":{"row":32,"column":37},"action":"insert","lines":["i"]},{"start":{"row":32,"column":37},"end":{"row":32,"column":38},"action":"insert","lines":["p"]},{"start":{"row":32,"column":38},"end":{"row":32,"column":39},"action":"insert","lines":["e"]},{"start":{"row":32,"column":39},"end":{"row":32,"column":40},"action":"insert","lines":["s"]}],[{"start":{"row":28,"column":43},"end":{"row":28,"column":44},"action":"remove","lines":[","],"id":216},{"start":{"row":28,"column":42},"end":{"row":28,"column":44},"action":"remove","lines":["''"]},{"start":{"row":28,"column":41},"end":{"row":28,"column":42},"action":"remove","lines":["T"]},{"start":{"row":28,"column":40},"end":{"row":28,"column":41},"action":"remove","lines":["E"]},{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"remove","lines":["G"]},{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"remove","lines":["'"]}],[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":["'"],"id":217}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":33},"end":{"row":2,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1572719289670,"hash":"9051992d0fde7d57fd408ad5ffb3ea991f3a4aef"}