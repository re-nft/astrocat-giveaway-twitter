import re

regex = r"0x\w*"

test_str = ("[START]@renftlabs @DogGodFrogLog 0xc8Bd3Bf698F4abb70e0eA333b071465e732cee4F[END]\n"
	"[START]@renftlabs 0x89beF75764f7E18f1FE53183536Fbe778A35040C[END]\n"
	"[START]@renftlabs 0xBC4e793D41d35DD5aDDE6748Db330Ed6579dED4B Discord #9639[END]\n"
	"[START]@renftlabs My Discord nick: BB#2507\n\n"
	"0x895B9C9cC6e94F803F64B15DCB08B36e4e302Eb8\n\n"
	"Thanks guys![END]\n"
	"[START]@renftlabs @queenwartooth 0x76Da9F88e63a85Ba8BFA19F3821D5A271753D3dc[END]\n"
	"[START]@renftlabs 0x4f0a1940de411285ad0455a7f40c81b5e0bc8492[END]\n"
	"[START]@renftlabs pretty sick designs! looking forward to the project :)\n\n"
	"0x336BFEdc1082515cc57C020eB51Fa59220e801b3[END]\n"
	"[START]@renftlabs 0x895B9C9cC6e94F803F64B15DCB08B36e4e302Eb8[END]\n"
	"[START]@renftlabs 0x41f6Df24FB1DB3584fC1269428e2f06789f8C0BD[END]\n"
	"[START]@renftlabs C'moooooon!!!\n"
	"0x127f892a760d19F5268A8468006659550B98FB6E \n"
	"Discord: dmitri#4929[END]\n"
	"[START]@renftlabs @Busayo26963937 Discord: graycii[END]\n"
	"[START]@renftlabs @Busayo26963937 0x149b78aDFe418d46Ef0424338aa565da7d5b5409[END]\n"
	"[START]@renftlabs 0x67c707dd30cfdc88d3cf77c7d90841d13e2f1451[END]\n"
	"[START]@renftlabs Like yr approach to NFTs here!\n"
	"0x1E6BB25d0068C11331c100e3c7eDb3bb8b98d042\n"
	"Discord joined[END]\n"
	"[START]@renftlabs Sweet, free NFT!\n"
	"0x0A4095a90bBe52625599EFd4B698d8d01B32676C\n"
	"Joined discord![END]\n"
	"[START]@renftlabs 0x1E56019C18E7Fe821896181a031AC75fD45c56F8[END]\n"
	"[START]@renftlabs 👍[END]\n"
	"[START]@renftlabs 0xeF77824A42200C897f724e50F382d4abA76CA7bC[END]\n"
	"[START]@renftlabs Thanks in advance\n\n"
	"0x840CAf73bdFdD52595Db90583B24FBACa3AB3a50[END]\n"
	"[START]@renftlabs This is way cool!\n"
	"Retweeted.\n"
	"Eth address:\n"
	"0x6119226BC6c6F063c418c4E905DD84b1C5Fb5459\n\n"
	"Discord:Bihep#7456[END]\n"
	"[START]@renftlabs 0x08bD1b3D29ec3FC1145fb684E0C041cCFe1299ef[END]\n"
	"[START]@renftlabs 0xaB38BB063C2F2D9520a4Db825602f23AB807fF13[END]\n"
	"[START]@renftlabs Nice project[END]\n"
	"[START]@renftlabs 😘 0xbba60570D0F850aaa99a9319224C1F64A583D2E7[END]\n"
	"[START]@renftlabs @house_thot 0x37644dede73feb30e844af27c54faa4aa9c92b6b\n\n"
	"Discord: Poninvest#6734[END]\n"
	"[START]@renftlabs This is awesome - can't wait.\n\n"
	"0xe246E7f15B92ED35560D7195A45057b75D3eC878[END]\n"
	"[START]@renftlabs hi, 0xBe44Acb7797880916cFc9C23a85A753b21c9aF80[END]\n"
	"[START]@renftlabs 0xC9E5A6155E05E9Ea2766D4c834428447f31225e7[END]\n"
	"[START]@renftlabs 0xd78910c72AD46747dfef5D11BF837637c1074A2a[END]\n"
	"[START]@renftlabs @freddycoen 0xEE4dB7C0c2648Cd9171d4217A1aE036D0Cae0E75[END]\n"
	"[START]@renftlabs 0x56Eff6730F1Ec041d43eD187ABdFdC044Cd9Ee29[END]\n"
	"[START]@renftlabs 0x8644A7780633a027F1923e0d15925Ed77FD60985 https://t.co/y58PMzUOSU[END]\n"
	"[START]@renftlabs 0xc28e6c37599c9b6e9ddd9008b90ce23d28b7a720\n"
	"@leo_mack @Igorivanovi4[END]\n"
	"[START]@renftlabs 0x3D6f6043fFC09AD396535CdFAcb6e4bC47668e02[END]\n"
	"[START]@renftlabs 0x70008F5937e2abbB679850ac67B851C869E83945\n\n"
	"Discord: ydujmmm#86165[END]\n"
	"[START]@renftlabs 0xDB63EB1d319d2948BE59A191179b835C6A8234b7[END]\n"
	"[START]@renftlabs 0x232F80c0e47Fbab2B7A227bD7b3a44bbddE15177[END]\n"
	"[START]@renftlabs @hamidkha123 0x234daE188cbFe8a050e83f326fB023B2d7B2Cd36\n\n"
	"Discord \n"
	"Zahra.p1400#6173[END]\n"
	"[START]@renftlabs 0xF464D1a37d8ef9449722f44a4EEb715c0e0acDb3[END]\n"
	"[START]@renftlabs 0x546C3E4cD18CFda1e70EaA70E8F2459231F582F5[END]\n"
	"[START]@renftlabs 0x75Eb6DB8dcFFef71b488fe945BB2BfE863a49263[END]\n"
	"[START]@renftlabs 0xc93aB154475C942aC6Eb29CEBc53360EDA6c367A[END]\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))