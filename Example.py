def main():


    x = int(input('Number of high range?: '))
    y = int(input('Number of low range?: '))
    z = int(input('Multiple to find?: '))
    show_multiples(x,y,z)

def show_multiples(x,y,z):

    for a in range(x,y,-1):

        if a % z == 0:

            print (a,end=' ')

            even_count = 0
            even_sum = 0
            odd_count = 0
            odd_sum = 0
    for num in range(x,y,-1):
        if num % z == 0 and num % 2 == 0:
            even_count += 1
            even_sum += num
    for number in range(x,y,-1):
        if number % z == 0 and number % 2 == 1:
            odd_count += 1
            odd_sum += number

    print(even_count,'even numbers total to',even_sum)
    print(odd_count,'odd numbers total to',odd_sum)

main()
