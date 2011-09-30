import string

#view.runCommand('ascii_colossal')
g_char_dict = None

# type credit: http://patorjk.com/software/taag/

caps = """ABCDEFGHIJKLMNOPQRSTUVWXYZ
        d8888 888888b.    .d8888b.  8888888b.  8888888888 8888888888  .d8888b.  888    888 8888888   888888 888    d8P  888      888b     d888 888b    888  .d88888b.  8888888b.   .d88888b.  8888888b.   .d8888b.  88888888888 888     888 888     888 888       888 Y88b   d88P Y88b   d88P 8888888888P 
       d88888 888  "88b  d88P  Y88b 888  "Y88b 888        888        d88P  Y88b 888    888   888       "88b 888   d8P   888      8888b   d8888 8888b   888 d88P" "Y88b 888   Y88b d88P" "Y88b 888   Y88b d88P  Y88b     888     888     888 888     888 888   o   888  Y88b d88P   Y88b d88P        d88P  
      d88P888 888  .88P  888    888 888    888 888        888        888    888 888    888   888        888 888  d8P    888      88888b.d88888 88888b  888 888     888 888    888 888     888 888    888 Y88b.          888     888     888 888     888 888  d8b  888   Y88o88P     Y88o88P        d88P   
     d88P 888 8888888K.  888        888    888 8888888    8888888    888        8888888888   888        888 888d88K     888      888Y88888P888 888Y88b 888 888     888 888   d88P 888     888 888   d88P  "Y888b.       888     888     888 Y88b   d88P 888 d888b 888    Y888P       Y888P        d88P    
    d88P  888 888  "Y88b 888        888    888 888        888        888  88888 888    888   888        888 8888888b    888      888 Y888P 888 888 Y88b888 888     888 8888888P"  888     888 8888888P"      "Y88b.     888     888     888  Y88b d88P  888d88888b888    d888b        888        d88P     
   d88P   888 888    888 888    888 888    888 888        888        888    888 888    888   888        888 888  Y88b   888      888  Y8P  888 888  Y88888 888     888 888        888 Y8b 888 888 T88b         "888     888     888     888   Y88o88P   88888P Y88888   d88888b       888       d88P      
  d8888888888 888   d88P Y88b  d88P 888  .d88P 888        888        Y88b  d88P 888    888   888        88P 888   Y88b  888      888   "   888 888   Y8888 Y88b. .d88P 888        Y88b.Y8b88P 888  T88b  Y88b  d88P     888     Y88b. .d88P    Y888P    8888P   Y8888  d88P Y88b      888      d88P       
 d88P     888 8888888P"   "Y8888P"  8888888P"  8888888888 888         "Y8888P88 888    888 8888888      888 888    Y88b 88888888 888       888 888    Y888  "Y88888P"  888         "Y888888"  888   T88b  "Y8888P"      888      "Y88888P"      Y8P     888P     Y888 d88P   Y88b     888     d8888888888 
                                                                                                      .d88P                                                                              Y8b                                                                                                              
                                                                                                    .d88P"                                                                                                                                                                                                
                                                                                                   888P"                                                                                                                                                                                                  """

lower = """abcdefghijklmnopqrstuvwxyz
          888                    888           .d888          888      d8b    d8b 888      888                                                                    888                                                               
          888                    888          d88P"           888      Y8P    Y8P 888      888                                                                    888                                                               
          888                    888          888             888                 888      888                                                                    888                                                               
  8888b.  88888b.   .d8888b  .d88888  .d88b.  888888  .d88b.  88888b.  888   8888 888  888 888 88888b.d88b.  88888b.   .d88b.  88888b.   .d88888 888d888 .d8888b  888888 888  888 888  888 888  888  888 888  888 888  888 88888888 
     "88b 888 "88b d88P"    d88" 888 d8P  Y8b 888    d88P"88b 888 "88b 888   "888 888 .88P 888 888 "888 "88b 888 "88b d88""88b 888 "88b d88" 888 888P"   88K      888    888  888 888  888 888  888  888 `Y8bd8P' 888  888    d88P  
 .d888888 888  888 888      888  888 88888888 888    888  888 888  888 888    888 888888K  888 888  888  888 888  888 888  888 888  888 888  888 888     "Y8888b. 888    888  888 Y88  88P 888  888  888   X88K   888  888   d88P   
 888  888 888 d88P Y88b.    Y88b 888 Y8b.     888    Y88b 888 888  888 888    888 888 "88b 888 888  888  888 888  888 Y88..88P 888 d88P Y88b 888 888          X88 Y88b.  Y88b 888  Y8bd8P  Y88b 888 d88P .d8""8b. Y88b 888  d88P    
 "Y888888 88888P"   "Y8888P  "Y88888  "Y8888  888     "Y88888 888  888 888    888 888  888 888 888  888  888 888  888  "Y88P"  88888P"   "Y88888 888      88888P'  "Y888  "Y88888   Y88P    "Y8888888P"  888  888  "Y88888 88888888 
                                                          888                 888                                              888           888                                                                       888          
                                                     Y8b d88P                d88P                                              888           888                                                                  Y8b d88P          
                                                      "Y88P"               888P"                                               888           888                                                                   "Y88P"           """

numbers = """1234567890
  d888    .d8888b.   .d8888b.      d8888  888888888   .d8888b.  8888888888  .d8888b.   .d8888b.   .d8888b.  
 d8888   d88P  Y88b d88P  Y88b    d8P888  888        d88P  Y88b       d88P d88P  Y88b d88P  Y88b d88P  Y88b 
   888          888      .d88P   d8P 888  888        888             d88P  Y88b. d88P 888    888 888    888 
   888        .d88P     8888"   d8P  888  8888888b.  888d888b.      d88P    "Y88888"  Y88b. d888 888    888 
   888    .od888P"       "Y8b. d88   888       "Y88b 888P "Y88b  88888888  .d8P""Y8b.  "Y888P888 888    888 
   888   d88P"      888    888 8888888888        888 888    888   d88P     888    888        888 888    888 
   888   888"       Y88b  d88P       888  Y88b  d88P Y88b  d88P  d88P      Y88b  d88P Y88b  d88P Y88b  d88P 
 8888888 888888888   "Y8888P"        888   "Y8888P"   "Y8888P"  d88P        "Y8888P"   "Y8888P"   "Y8888P"  
                                                                                                            
                                                                                                            
                                                                                                            """


symbols = """!@#$%^&*()
 888  .d8888888b.    888  888        88     d88b   d88P    o     .d8888b.                      .d88 88b.   
 888 d88P"   "Y88b   888  888    .d88888b.  Y88P  d88P    d8b   d88P  "88b           o        d88P" "Y88b  
 888 888  d8b  888 888888888888 d88P 88"88b      d88P    d888b  Y88b. d88P          d8b      d88P     Y88b 
 888 888  888  888   888  888   Y88b.88         d88P    d8P"Y8b  "Y8888P"          d888b     888       888 
 888 888  888bd88P   888  888    "Y88888b.     d88P             .d88P88K.d88P  "Y888888888P" 888       888 
 Y8P 888  Y8888P"  888888888888      88"88b   d88P              888"  Y888P"     "Y88888P"   Y88b     d88P 
  "  Y88b.     .d8   888  888   Y88b 88.88P  d88P  d88b         Y88b .d8888b     d88P"Y88b    Y88b. .d88P  
 888  "Y88888888P"   888  888    "Y88888P"  d88P   Y88P          "Y8888P" Y88b  dP"     "Yb    "Y88 88P"   
                                     88                                                                    
                                                                                                           
                                                                                                           """

symbols2 = """`~-_=+
 d8b                                            
 Y88                                            
  Y8  d888b  d88                                
   Y d888888888P                 888888   888   
     88P  Y888P                         8888888 
                 888888          888888   888   
                                                
                        88888888                
                                                
                                                
                                                """

symbols3 = """[]{}\|;':",./<>?
 8888888 8888888   .d888 888b.  Y88b        888     d8b     88 88                d88P    d88P Y88b     .d8888b.  
 888         888  d88P"   "Y88b  Y88b       888     88P     8P 8P               d88P    d88P   Y88b   d88P  Y88b 
 888         888  888       888   Y88b      888     8P      "  "               d88P    d88P     Y88b       .d88P 
 888         888 .888       888.   Y88b     888 d8b "   d8b                   d88P    d88P       Y88b    .d88P"  
 888         888 888(       )888    Y88b        Y8P     Y8P                  d88P     Y88b       d88P    888"    
 888         888 "888       888"     Y88b   888                             d88P       Y88b     d88P     888     
 888         888  888       888       Y88b  888 d8b     d8b       d8b d8b  d88P         Y88b   d88P              
 8888888 8888888  Y88b.   .d88P        Y88b 888 88P     Y8P       88P Y8P d88P           Y88b d88P       888     
                   "Y888 888P"              888 8P                8P                                             
                                                "                 "                                              
                                                                                                                 """


def run(lines_lst):
    if g_char_dict is None: load()
    lst = []
    for l in lines_lst:
        l = l.strip()
        lst.append(l)
        lst.append(block_text(l, g_char_dict))

    return string.join(lst, "\n\n")


def parse(txt, debug_print = False):
    txt = txt.split("\n")
    chars = txt[0]
    if debug_print: print "CHARS:", chars
    char_dict = {}
    gap_list = []

    idx = 1
    done = False
    while not done:
        all_gaps = True
        for i in xrange(1, len(txt)):
            if txt[i][idx] != " ": all_gaps = False
            done = done or (idx+1 >= len(txt[i]))
        if all_gaps: gap_list.append(idx)
        idx += 1

    if len(chars) != len(gap_list): print "ASCII COLOSSAL: ERROR not enough chars found for '%s'" % chars
    last_idx = 0
    for c, g in zip(chars, gap_list):
        if debug_print: print c, g
        lines_list = []
        for i in xrange(1, len(txt)):
            lines_list.append(txt[i][last_idx:g])
        last_idx = g
        char_dict[c] = lines_list
    return char_dict


def block_text(txt, char_dict):
    char_list = []
    line_count = None
    for c in txt:
        l = char_dict.get(c, None)
        if not l is None:
            char_list.append(l)
            line_count = len(l)
    lines_list = []
    for l in xrange(line_count):
        line = string.join(map(lambda x: x[l], char_list), "")
        lines_list.append(line)
    return string.join(lines_list, "\n")


def load(debug_print = False):
    global g_char_dict
    print "ASCII COLOSSAL: Loading"
    char_dict = {}
    rc = parse(caps, debug_print = debug_print); char_dict.update(rc)
    rc = parse(lower, debug_print = debug_print); char_dict.update(rc)
    rc = parse(numbers, debug_print = debug_print); char_dict.update(rc)
    rc = parse(symbols, debug_print = debug_print); char_dict.update(rc)
    rc = parse(symbols2, debug_print = debug_print); char_dict.update(rc)
    rc = parse(symbols3, debug_print = debug_print); char_dict.update(rc)
    g_char_dict = char_dict

    #add space here
    l = char_dict.get("-", None)
    if not l is None:
        height = len(l)
        width = len(l[0])
        g_char_dict[" "] = [" " * width] * height


if __name__ == "__main__":
    load(debug_print = True)
    print block_text("#@$(", g_char_dict)


if __name__ != "__main__":
    import sublime, sublime_plugin

    # Extends TextCommand so that run() receives a View to modify.  
    class ascii_colossal(sublime_plugin.TextCommand):
        def run(self, edit):  
            view = self.view
            print "ascii colossal"
            # Walk through each region in the selection  
            for region in view.sel():  
                if region.empty():
                    print "error: nothing selected"
                else:
                    # print "create instance 1", dir(region)
                    block = view.line(region)
                    lines_block = view.substr(block)
                    # print "lines_block ====>", lines_block
                    lines_lst = lines_block.split('\n')
                    # print "lines_lst ====>", lines_lst
                    lst = run(lines_lst)
                    # print lst
                    # print dir(view)
                    # print help(view)
                    new_str = lst

                    # view.insert(block.end(), new_str)
                    # view.insert(block.end(), '\n')
                    
                    view.replace(edit, region, new_str)

