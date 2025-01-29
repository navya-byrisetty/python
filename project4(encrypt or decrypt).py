alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type 'encode' to encrypt ,type 'decode' to decrypt:").lower()
text=input("type your message:").lower()
shift=int(input("type the key number"))
def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    for letter in original_text:
        
        if encode_or_decode=="decode":
            shift_amount*=-1
        shifted_position=alphabet.index(letter)+shift_amount
        shifted_position %=len(alphabet)
        output_text+=alphabet[shifted_position]
    print(f"here is the {encode_or_decode}  result is:{output_text}")
caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    

    
