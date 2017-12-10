# Mixed paper and cardboard:
# -newspapers, magazines, catalogs
# -receipts
# -wrapping paper
# -envelopes, including window envelopes
# -soft-cover books (no hardcover books)
# -paper bags
# -cardboard boxes, including pizza boxes (first throw away the liner)
# -egg cartons
# -paper towel rolls
# -Do not include: food-contaminated paper, hardcover books, bubble wrap, photographs, tissues, napkins, paper towels, waxed or plastic-coated paper

# 'rigid plastic caps': ['yogurt container', 'dairy tub', 'cookie tray insert']
# 			'rigid plastic food containers':
# 			'rigid plastic non-food containers':
# 			'rigid plastic packaging':
# 			'rigid plastic housewares':
# 			'bulk rigid plastic':
 # do not recycled: wax coating, plastic coating, anything too soiled 
 #['If it is plastic number 3, 6, or 7 it cannot be recycled.']
 #plastic/can empty and rinse container before placing in the bin
			
bluebin = { 
			['plastic water bottle', 'plastic bottle', 'plastic jug', 'plastic jar', 
			 'yogurt container', 'dairy tub', 'cookie tray insert'] : 'plastic'
			
			['glass bottle', 'glass jar'] : 'glass'

			['milk carton', 'juice boxes'] : 'carton'

			['metal cans', 'soup can', 'pet food can', 'empty aerosol can', 'dried-out paint can', 
			 'aluminum foil wrap', 'aluminum tray', 'wire hanger', 'metal pot', 'metal tools', 'curtain rod', 
			 'knife'] : 'metal'

			}

greenbin = { ['newspapers', 'magazines', 'catalogs,receipts', 'wrapping paper', 'envelopes'
			'including window envelopes', 'soft-cover books', 'paper bags', 'cardboard boxes', 
			'egg cartons', 'paper towel rolls', 'pizza box', 'shoe box','corrugated cardboard', 
			'shredded paper', 'scrap paper', 'cards', 'mail', 'paper bags', 'sticky notes', 
			'copy paper'] : ['This item should go into the mixed paper and cardboard recycling bin']
}
#if pizza box prompt used to throw away the liner in the trash

trash = { ['hardcover books', 'napkins', 'paper towels', 'tissues', 'candy wrappers', 'photographs', 
			'bubble wrap', 'straw', 'batteries','plastic bags', 'wrappers', 'pouches', 'squeeze tubes', 
			'foam', 'styrofoam', 'wax coating', 'plastic coating'] : 'This item should go into the trash bin'
	
}

item = {
         'plastic': ['plastic water bottle, plastic bottle, plastic jug, plastic jar, rigid plastic food container, yogurt container, dairy tub, cookie tray insert, plastic take-out container, ']
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                    """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
         } 

def post_facebook_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    item_text = ''
    for token in tokens:
        if token in item:
            item_text = random.choice(item[token])
            break
    if not item_text:
        item_text = "I didn't understand! Send 'stupid', 'fat', 'dumb' for a Yo Mama joke!" 

    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'EAAc1vc2ZC7KUBAKRrfvHBZAkmfJqBZAt76sOvjMvwpyUqaWveJHgEEdZAL2ZBTh3Ufz9g9mA4rBkt2vo4qaQyJnzR68ceFTiefpFKZA7eLEGa6VdZAWTcSCFqyep28DXjybn3TZCgtMaZCYipgZBIByCVXwZB3iZA4jhjqKfqZApXHngKcgZDZD'} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    item_text = 'Hello! '+user_details['first_name']+'..! ' + item_text
    
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAc1vc2ZC7KUBAKRrfvHBZAkmfJqBZAt76sOvjMvwpyUqaWveJHgEEdZAL2ZBTh3Ufz9g9mA4rBkt2vo4qaQyJnzR68ceFTiefpFKZA7eLEGa6VdZAWTcSCFqyep28DXjybn3TZCgtMaZCYipgZBIByCVXwZB3iZA4jhjqKfqZApXHngKcgZDZD'
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":item_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())