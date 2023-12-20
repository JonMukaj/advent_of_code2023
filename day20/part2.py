"""
--- Part Two ---
The final machine responsible for moving the sand down to Island Island has a module attached named rx. The machine turns on when a single low pulse is sent to rx.

Reset all modules to their default states. Waiting for all pulses to be fully handled after each button press, what is the fewest number of button presses required to deliver a single low pulse to the module named rx?
"""

def conj_empty(conj_patterns, broadcasters, conjunctions, flipflops, button, low, high, total):
    while conj_patterns:
        button += 1; 
        low += 1
        queue = [{"broadcaster" : (0, "button")}]
        while queue:
            receiver, (signal, origin) = queue.pop(0).popitem()
            if receiver not in broadcasters: 
                continue
            if receiver in conjunctions: 
                conjunctions[receiver][origin] = signal
            if receiver in flipflops:
                if signal: 
                    continue
                else:
                    flipflops[receiver] = not flipflops[receiver]
            for remote, signal_func in broadcasters[receiver].items():
                queue.append({remote : (sent := signal_func(signal), receiver)})
                if sent == 1: 
                    high += 1
                else:
                    low += 1
            if receiver in conj_patterns and sent: 
                conj_patterns.remove(receiver)
                total *= button
    return total   
            
def solve():
    broadcasters, conjunctions, flipflops, relevant, queue, low, high, button, total = {}, {}, {}, {}, {"rx"}, 0, 0, 0, 1
    for broadcaster, receivers in [x.split(" -> ") for x in input.splitlines()]:
        b, receivers = broadcaster[1:], receivers.split(", ")
        if broadcaster == "broadcaster":  
            broadcasters[broadcaster] = {x : (lambda y: y) for x in receivers}
        elif broadcaster.startswith("&"): 
            broadcasters[b] = {x : (lambda y, b=b: set(conjunctions[b].values()) != {1}) for x in receivers}
            conjunctions[b] = {}
        elif broadcaster.startswith("%"): 
            broadcasters[b] = {x : (lambda y, b=b: flipflops[b]) for x in receivers}
            flipflops[b] = 0
    for k, v in broadcasters.items():
        for x in v:
            if x in conjunctions: 
                conjunctions[x][k] = 0
    while queue:
        current = queue.pop()
        relevant[current] = nxt = [k for k, v in broadcasters.items() if current in v]
        for x in nxt:
            if x not in relevant: 
                queue.add(x)
    conj_patterns = {x for x in set(sum(relevant.values(), [])) if x in conjunctions}
    return conj_empty(conj_patterns, broadcasters, conjunctions, flipflops, button, low, high, total)


file_path = "input.txt"
try:
    with open(file_path, "r") as file: 
        input = file.read()
        print("Total:", solve())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")