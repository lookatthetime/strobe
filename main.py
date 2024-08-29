import asyncio

async def main():
    from modules import latt
    if latt.testPG():
        import pygame
    else:
        exit(1)
    from sys import exit
    from random import randint
    from time import sleep
    # try:
    #     from mod import items
    #     if latt._question("Are you sure you would like to load a mod?"):
    #         del items
    #         import mod
    #         class m:
    #             loaded = True
    #             modInits = []
    #             info = {}
    #         latt.splash()
    #     else:
    #         del items
    #         class m:
    #             loaded = False
    # except:
    #     class m:
    #         loaded = False
    
    class m:
        loaded = False

    print("LOG: imports complete")

    # latt.betaWarning()

    VER_NAME = "strobe 2.0"

    if m.loaded:
        for item in mod.items:
            m.modInits.append(item())

    # latt.winPos(100, 100)

    pygame.init()

    print(pygame.get_sdl_version())

    WIDTH, WIDTH = 500, 500

    fps = 120
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, WIDTH), pygame.NOFRAME)
    print(pygame.display.Info())
    if m.loaded:
        pygame.display.set_caption(f'* {VER_NAME}')
    else:
        pygame.display.set_caption(VER_NAME)

    pTex = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/orb_mid.png")))
    pLightTex = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/light.png"))).convert()
    pLightTex.set_alpha(50)

    streakTex = pygame.image.load(__file__.replace("main.py", "assets/streak.png"))

    lightStreakTex = pygame.image.load(__file__.replace("main.py", "assets/light_streak.png"))

    b_1 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_0.png"))))
    b_2 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_1.png"))))
    b_3 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_2.png"))))
    b_4 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_3.png"))))
    b_5 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_4.png"))))
    b_6 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_5.png"))))
    b_7 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/blast_6.png"))))

    bar_1 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_0.png")))
    bar_2 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_1.png")))
    bar_3 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_2.png")))
    bar_4 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_3.png")))
    bar_5 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_4.png")))
    bar_6 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_5.png")))
    bar_7 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/bar_6.png")))

    slide_1 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/slide_0.png")))
    slide_2 = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/slide_1.png")))

    mbTex = pygame.transform.scale2x(pygame.image.load(__file__.replace("main.py", "assets/mb.png"))).convert()

    pygame.display.set_icon(pygame.image.load(__file__.replace("main.py", "assets/orb.png")))

    title_font = pygame.font.Font('freesansbold.ttf', 150)
    main_font = pygame.font.Font('freesansbold.ttf', 24)
    small_font = pygame.font.Font('freesansbold.ttf', 12)

    print("LOG: all images fetched, fonts set up")

    # pygame.mouse.set_cursor(SYSTEM_CURSOR_WAIT)

    ss_text = main_font.render("look at the time studios presents", True, (255, 255, 255))
    ssIter = 0

    while True:
        ssIter += 1

        screen.blit(ss_text, (50, 238))

        if ssIter == 60:
            screen = pygame.display.set_mode((WIDTH, WIDTH))
        elif ssIter == 100:
            break

        pygame.display.flip()
        await asyncio.sleep(0)

    title_text = title_font.render("strobe", True, (255, 255, 255))
    start_text = main_font.render("press space", True, (255, 255, 255))
    blur_text = small_font.render("press b to toggle blur", True, (255, 255, 255))

    screen.fill((0, 0, 0))

    runConst = False

    noClip = False

    blur = 200

    pygame.mouse.set_cursor()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            # if latt._question("Activate Blur?"):
            #     try:
            #         blur = int(latt.askInt("strobe", "Blur Amount:", iv=80))
            #     except Exception as e:
            #         print(f"WARNING: blur failed to activate - {e}")
            blur = 80
        if keys[pygame.K_SPACE]:
            break
        if keys[pygame.K_ESCAPE]:
            exit(1)
        if keys[pygame.K_SLASH]:
            # runConst = latt.run("strobe dev console", "/", prompt="Enter Console Command to Permarun")
            # noClip = latt._question("Run with NoClip?")
            pass

        screen.blit(title_text, (10, 10))
        screen.blit(start_text, (10, 300))
        screen.blit(blur_text, (10, 340))

        pygame.display.flip()
        await asyncio.sleep(0)

    print("LOG: starting game...")

    mbTex.set_alpha(blur)

    pX = 0
    pY = 0

    blastPos = []
    blastIter = 0
    blastAnim = [b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1,
                b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1,b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1, b_1,
                b_1, b_1, b_1, b_1, b_1, b_2, b_2, b_2, b_2, b_3, b_4, b_5, b_6, b_7]

    isBar = -1
    barIter = 0
    barAnim = [bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1, bar_1,
            bar_1, bar_1, bar_1, bar_1, bar_2, bar_3, bar_4, bar_5, bar_5, bar_5, bar_5, bar_5, bar_5, bar_5, bar_5,
            bar_5, bar_5,bar_6, bar_7] # act like 20 bar_1s

    streaks = []
    streakIter = 0

    lightStreaks = []
    lightStreakIter = 0

    slideX = 0
    slideFinalX = 0
    isSlide = -1
    slideIter = 0
    slideAnim = [slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1,
                slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1,
                slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1, slide_1,
                slide_2, slide_2, slide_2, slide_2, slide_2, slide_2, slide_2, slide_2, slide_2, slide_2,
                slide_2, slide_2, slide_2, slide_2, slide_2]

    screenShake = [0, 0]

    score = 0

    running = True

    # def touchingPlayer(pX, pY, x, y, xLen, yLen):
    #     for iX in range(xLen):
    #         for iY in range(yLen):
    #             if (x + iX) > (pX + 8) and (x + iX) < (pX + 24) and (y + iY) > (pY + 8) and (y + iY) < (pY + 24):
    #                 return True
    #     return False

    def touchingPlayer(pX, pY, x, y, xLen, yLen):
        if pX < (x + xLen) and (pX + 32) > x and pY < (y + yLen) and (pY + 32) > y:
            return True
        return False

    print("LOG: set up, starting game")

    # Game loop
    while True:
        score = 0

        running = True
        main = pygame.Surface(screen.get_size())
        while running:
            fpsClock.tick(fps)

            main.blit(mbTex, (0, 0))

            # main.fill((10, 10, 10))

            # Update

            fps = 120

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(1)
            
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and pY > 0:
                pY -= 8
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and pY < 468:
                pY += 8
            if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and pX > 0:
                pX -= 8
            if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and pX < 468:
                pX += 8
            if keys[pygame.K_ESCAPE]:
                print("LOG: game session ended")
                exit(1)
            
            if keys[pygame.K_SLASH] or runConst: # Capture and Process Commands
                pass
                # if pygame.display.get_caption()[0] == VER_NAME:
                #     pygame.display.set_caption(f"{VER_NAME} - dev")
                # if runConst:
                #     run_val = runConst
                # else:
                #     run_val = latt.run("strobe dev console", "/")
                #     if not run_val:
                #         run_val = ""
                # run_val = run_val.lower()
                # vals = {"px":str(pX), "py":str(pY), "score":str(int(score))}
                # for key in vals:
                #     run_val = run_val.replace(f"${key}", str(vals[key]))
                # if run_val.startswith("/name "):
                #     if run_val.replace("/name ", "") != VER_NAME:
                #         pygame.display.set_caption(run_val.replace("/name ", "", 1))
                #     else:
                #         print("LOG: nice try >:)")
                # elif run_val.startswith("/spawn "):
                #     try:
                #         if run_val.__contains__("blast"):
                #             coord = run_val.replace("/spawn blast ", "")
                #             blastPos.append([int(coord), 0])
                #             print("LOG: blast created")
                #         elif run_val.__contains__("lightstreak"):
                #             coord = run_val.replace("/spawn lightstreak ", "")
                #             lightStreaks.append([500, int(coord)])
                #             print("LOG: lightstreak created")
                #         elif run_val.__contains__("streak"):
                #             coord = run_val.replace("/spawn streak ", "")
                #             streaks.append([500, int(coord)])
                #             print("LOG: streak created")
                #         elif run_val.__contains__("slide"):
                #             coord = run_val.replace("/spawn slide ", "")
                #             slideFinalX = int(coord)
                #             slideX = slideFinalX
                #             isSlide = 0
                #             print("LOG: slide created")
                #         else:
                #             print("LOG: spawn type unspecified")
                #     except Exception as e:
                #         print(f"WARNING: spawn command failed - {e}")
                # elif run_val == "/noclip":
                #     noClip = not noClip
                # elif run_val.startswith("/tp "):
                #     try:
                #         coords = run_val.replace("/tp ", "").split(" ")
                #         pX, pY = int(coords[0]), int(coords[1])
                #     except Exception as e:
                #         print(f"WARNING: tp command failed - {e}")
                # else:
                #     print("LOG: unknown command")
            
            if pY < 0 or pY > 485 or pX < 0 or pX > 485:
                pX, pY = 0, 0

            # Draw
            main.blit(pLightTex, (pX - 16, pY - 16)) # Draw Character Light

            if streakIter == 8: # Create and Draw streaks
                streaks.append([500, randint(0, 500)])
                streakIter = 0
            else:
                streakIter += 1
            
            try:
                if streaks[0][0] == -75:
                    streaks.pop(0)
            except:
                pass

            cur_iter = 0
            for i in streaks:
                main.blit(streakTex, (i[0], i[1]))
                streaks[cur_iter][0] -= 5
                cur_iter += 1

            
            if barIter > 150 and randint(1, 50) == 1 and isSlide == -1: # Create and Draw Bars
                isBar = 0
                barIter = 0
            else:
                barIter += 1
            
            if isBar == 34:
                isBar = -1
            
            if isBar > -1:
                main.blit(barAnim[isBar], (0, 0))
                if isBar > 20:
                    if pX < 200:
                        if not noClip:
                            running = False
                    elif pX > 268:
                        if not noClip:
                            running = False
                isBar += 1
                screenShake = [randint(-10, 10), randint(-10, 10)]
            

            if slideIter > 200 and randint(1, 70) == 1 and isBar == -1: # Create and Draw Slides
                slideFinalX = randint(200, 350)
                slideX = slideFinalX
                isSlide = 0
                slideIter = 0
            else:
                slideIter += 1
            
            if isSlide == 45:
                isSlide = -1
            
            if isSlide > -1:
                if isSlide == 29:
                    slideX = 0
                if isSlide > 30 and isSlide <= 40:
                    slideX += slideFinalX / 10
                    fps = 90
                    if pX < slideX:
                        if not noClip:
                            running = False
                elif isSlide > 35:
                    slideX = slideFinalX
                    if pX < slideX:
                        if not noClip:
                            running = False
                main.blit(slideAnim[isSlide], (slideX - 500, 0))
                isSlide += 1
                screenShake = [randint(-15, 15), randint(-15, 15)]


            if lightStreakIter == 65: # Create and Draw Light Streaks
                lightStreaks.append([500, randint(0, 500)])
                lightStreakIter = 0
            else:
                lightStreakIter += 1
            
            try:
                if lightStreaks[0][0] == -75:
                    lightStreaks.pop(0)
            except:
                pass

            cur_iter = 0
            for i in lightStreaks:
                main.blit(lightStreakTex, (i[0], i[1]))
                lightStreaks[cur_iter][0] -= 5
                if touchingPlayer(pX, pY, i[0], i[1], 75, 6):
                    if not noClip:
                        running = False
                cur_iter += 1


            if blastIter == 50 and not randint(1, 5) == 1: # Create and Draw Blasts
                if randint(1, 2) == 1:
                    blastPos.append([(pY + randint(-75, 75)), 0])
                else:
                    blastPos.append([randint(0, 500), 0])
                if randint(1, 8) == 1:
                    blastPos.append([(pY + randint(-75, 75)), 0])
                blastIter = 0
            elif blastIter == 50:
                blastPos.append([(pY + 75), 0])
                blastPos.append([(pY - 75), 0])
                blastIter = 0
            else:
                blastIter += 1
            
            try:
                if blastPos[0][1] == 55:
                    blastPos.pop(0)
            except:
                pass

            try:
                if blastPos[0][1] == 55:
                    blastPos.pop(0)
            except:
                pass
            
            cur_iter = 0
            for i in blastPos:
                main.blit(blastAnim[i[1]], (0, i[0]))
                blastPos[cur_iter][1] += 1
                if i[1] == 45:
                    screenShake = [randint(-2, 2), randint(-2, 2)]
                if i[1] > 45:
                    screenShake = [randint(-5, 5), randint(-5, 5)]
                    # print(i[0])
                    # print(pY)
                    # if pY < (i[0] + 32) and pY > (i[0]):
                    fps = 70
                    if touchingPlayer(pX, pY, 0, i[0], 500, 92):
                        if not noClip:
                            running = False
                cur_iter += 1
            
            m.info = {"pX":pX, "pY":pY, "score":score, "ss":screenShake, "fps":fps}

            if m.loaded:
                for item in m.modInits:
                    main.blit(item.animate(), item.update())
                    collided = item.collide()
                    if touchingPlayer(pX, pY, collided[0][0], collided[0][1],
                                    collided[1][0], collided[1][1]):
                        outcome = collided[2]()
                        if not outcome:
                            if not noClip:
                                running = False
                        try:
                            pX = outcome["pX"]
                            pY = outcome["pX"]
                            score = outcome["score"]
                            screenShake = outcome["ss"]
                            fps = outcome["fps"]
                        except:
                            pass


            main.blit(pTex, (pX, pY)) # Draw Character

            # if score >= 500:
            #     if randint(0, 1) == 0:
            #         screenShake[0] += 50
            #     else:
            #         screenShake[0] += 45

            score_text = main_font.render(str(int(score)), True, (16, 181, 178))
            main.blit(score_text, (10, 10))

            screen.blit(main, (screenShake[0], screenShake[1]))
            screenShake = [0, 0]

            pygame.display.flip()
            fpsClock.tick(fps)
            score += 1.25
            await asyncio.sleep(0)

        end_text = title_font.render(str(int(score)), True, (16, 181, 178))
        close_game_text = main_font.render("press space to retry  -  escape to close", True, (200, 200, 200))

        print("LOG: end screen created")

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(1)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                print("LOG: game session ended")
                exit(1)
            if keys[pygame.K_SPACE]:
                running = False
            if keys[pygame.K_SLASH]:
                pass
                # runConst = latt.run("strobe dev console", "/", prompt="Enter Console Command to Permarun")
                # noClip = latt._question("Run with NoClip?")

            screen.blit(end_text, (10, 10))
            screen.blit(close_game_text, (10, 300))

            pygame.display.flip()
            await asyncio.sleep(0)
        
        print("LOG: starting game...")

        pX = 0
        pY = 0

        blastPos = []
        blastIter = 0

        isBar = -1
        barIter = 0

        streaks = []
        streakIter = 0

        lightStreaks = []
        lightStreakIter = 0

        slideX = 0
        slideFinalX = 0
        isSlide = -1
        slideIter = 0

        screenShake = [0, 0]

        score = 0

        if m.loaded:
            for item in m.modInits:
                item.reset()

        running = True

if __name__ == "__main__":
    asyncio.run(main())